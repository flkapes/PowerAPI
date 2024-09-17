from celery import shared_task
import subprocess
import re
import psutil
import time
from .powerapi.models import HDDModel, CPUModel
from .powerapi.wattage_calc import calculate_disk_powerdraw
from django.utils import timezone


def sanitize_input(string_to_clean):
    """
    Cleans input using REGEX to remove /dev/ prefix or the numbered suffix associated with a partition.
    """
    drive_only = r"sd[A-Za-z]{1}"
    output = re.findall(drive_only, string_to_clean)
    return output


def get_drive_io(drive_name: str) -> float:
    """Calls collectl in a subprocess to get the disk I/O data for all drives, parses lines to extract I/O stats."""
    time.sleep(0.1)
    sanitized_drive = sanitize_input(drive_name)[0]
    if sanitized_drive is None:
        print(
            f"Could not verify drive {drive_name}, please use either the /dev/sdX or sdX format."
        )
        return

    # Command to collect disk stats from collectl
    io_command = ["collectl", "-i", "5", "-c", "1", "-sD"]

    process = subprocess.Popen(
        io_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        drive_lines = [
            line for line in stdout.decode().splitlines() if sanitized_drive in line
        ]
        if drive_lines:
            try:
                # Split the line and get the Pct Util value (last column)
                io_stats = drive_lines[0].split()
                pct_util = float(io_stats[-1])  # Last column is the Pct Util value
                return pct_util
            except ValueError:
                print(f"Unexpected data format for drive {drive_name}.")
        else:
            print(f"Drive {drive_name} not found in collectl output.")
    else:
        print(f"Error executing collectl: {stderr.decode().strip()}")

    return None


def get_device_by_uuid(uuid):
    # Use blkid to find the device path by UUID
    cmd = ["blkid", "-o", "device", "-t", f"PARTUUID={uuid}"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        device = stdout.decode().strip()
        return device
    else:
        print(f"Error: {stderr.decode().strip()}")
        return None


def get_cpu_power():
    cpu_command = ["likwid-powermeter", "-s", "10s"]
    process = subprocess.Popen(
        cpu_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        cpu_lines = stdout.decode().splitlines()
        
        # Find all occurrences of "Power consumed: X Watt"
        power_values = re.findall(r"Power consumed:\s*([\d.]+)\s*Watt", " ".join(cpu_lines))
        
        # If power values were found, sum them up
        if power_values:
            total_power = sum(float(power) for power in power_values)
            print(power_values, total_power)
            return total_power
        else:
            print("No power values found.")
            return None
    else:
        print(f"Error occurred: {stderr.decode()}")
        return None

@shared_task
def update_cpu_power(cpu_id):
    power_draw = get_cpu_power()

    if power_draw is not None:
        try:
            cpu = CPUModel.objects.get(cpu_id=cpu_id)
            cpu.estimated_powerdraw = power_draw
            cpu.current_load = psutil.cpu_percent()
            cpu.last_updated = timezone.now()
            cpu.save()
            return f"Updated CPU {cpu_id} with power draw: {power_draw}."
        except CPUModel.DoesNotExist:
            return f"CPU ID: {cpu_id} does not exist in the database."
    else:
        return f"Failed to retrieve CPU Power Data for CPU {cpu_id}."

@shared_task
def update_drive_io(drive_uuid):
    drive_name = get_device_by_uuid(drive_uuid)
    io_value = get_drive_io(drive_name)

    if io_value is not None:
        try:
            drive = HDDModel.objects.get(disk_uuid=drive_uuid)
            drive.current_io = io_value
            drive.estimated_powerdraw = calculate_disk_powerdraw(
                drive.model_number, io_value
            )
            drive.last_updated = timezone.now()
            drive.save()
            return f"Updated drive {drive_uuid} with IO Value: {io_value}."
        except HDDModel.DoesNotExist:
            return f"Drive UUID: {drive_uuid} does not exist in the database."
    else:
        return f"Failed to retrieve IO data for drive {drive_uuid}."
