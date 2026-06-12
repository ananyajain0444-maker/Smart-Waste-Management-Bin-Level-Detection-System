def check_alert(fill_percentage):

    if fill_percentage >= 90:
        return "Full"

    elif fill_percentage >= 75:
        return "Warning"

    else:
        return "Normal"