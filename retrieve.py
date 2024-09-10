import subprocess
import re

def sanitize_input(string_to_clean):
    drive_only = r"sd[A-Za-z]{1}"
    output = re.findall(drive_only, string_to_clean)
    return output


def get_drive_io(drive_name: str) -> float:
    """Calls iostat in a shell subprocess to get the IO data for a specific drive."""

    sanitized_drive = sanitize_input(drive_name)[0]
    if sanitized_drive is None:
        print(f"Could not verify drive {drive_name}, please use either the /dev/sdX or sdX format.")
        return

    io_command = f"iostat -xd | grep '{sanitized_drive}' | awk '{{print $NF}}'"

    process = subprocess.Popen(io_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
        
    if process.returncode == 0:
        try:
            io_decimal = stdout.decode().strip()
            print(f"{sanitized_drive}: {io_decimal}")
            return io_decimal
        except ValueError as e:
            print(f"Please make sure the refrenced drive {drive_name} actually exists.")
    else:
        print(f"Error with {drive_name}: {stderr.decode().strip()}")