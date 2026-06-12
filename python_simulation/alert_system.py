def check_alert(fill_percentage):
    if fill_percentage >= 90:
        return "ALERT: Bin Full!"
    elif fill_percentage >= 75:
        return "Warning: Near Full"
    else:
        return "Normal"