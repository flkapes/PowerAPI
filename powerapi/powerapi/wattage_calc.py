disk_power_draw = {
    "HUH721212ALE601": {"peak": 6.9, "idle": 5.0},
    "WD HGSTHUH721212AL": {"peak": 6.9, "idle": 5.0},
}


def calculate_disk_powerdraw(model, io):
    """This function simply performs basic linear interpolation using the HDD's known power draw at idle and peak load to
    estimate the power consumption of a HDD given its model number and I/O load %age.
    """
    power_draw = (
        disk_power_draw[model]["idle"]
        + ((disk_power_draw[model]["peak"] - disk_power_draw[model]["idle"]) / 100) * io
    )
    return (
        round(power_draw, 2)
        if round(power_draw, 2) > disk_power_draw[model]["idle"]
        else disk_power_draw[model]["idle"]
    )
