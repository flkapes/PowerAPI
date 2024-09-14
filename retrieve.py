import subprocess
import re, time

def sanitize_input(string_to_clean):
    drive_only = r"sd[A-Za-z]{1}"
    output = re.findall(drive_only, string_to_clean)
    return output


def get_drive_io(drive_name: str) -> float:
    """Calls iostat in a subprocess to get the disk IO data for all drives, parses lines using python instead of shell to reduce
    risk of shell-injection attacks."""
    time.sleep(0.1)
    sanitized_drive = sanitize_input(drive_name)[0]
    if sanitized_drive is None:
        print(f"Could not verify drive {drive_name}, please use either the /dev/sdX or sdX format.")
        return

    io_command = ["iostat", "-xd"]

    process = subprocess.Popen(io_command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
        
    if process.returncode == 0:
        drive_lines = [line for line in stdout.decode().splitlines() if drive_name in line]
        if drive_lines:
            try:
                io_stat = drive_lines[0].split()[-1]
                io_decimal = float(io_stat)
                print(f"{sanitized_drive}: {io_decimal}")
                return io_decimal
            except ValueError:
                print(f"Unexpected data format for drive {drive_name}.")
        else:
            print(f"Drive {drive_name} not found in iostat output.")
    else:
        print(f"Error executing iostat: {stderr.decode().strip()}")

get_drive_io("sdb")
print([f"{get_drive_io("sda")} {get_drive_io("sdd")} {get_drive_io("sdc")} {get_drive_io("sdb")}" for _ in range(1000)])