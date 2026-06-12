BIN_HEIGHT = 100

def calculate_fill_percentage(distance):
    fill_percentage = ((BIN_HEIGHT - distance) / BIN_HEIGHT) * 100

    if fill_percentage < 0:
        fill_percentage = 0

    return round(fill_percentage, 2)

def get_bin_status(fill_percentage):
    if fill_percentage <= 25:
        return "Empty"
    elif fill_percentage <= 50:
        return "Low"
    elif fill_percentage <= 75:
        return "Medium"
    elif fill_percentage <= 90:
        return "High"
    else:
        return "Critical"