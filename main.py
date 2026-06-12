import pandas as pd

from python_simulation.data_generator import generate_sensor_data

from python_simulation.fill_level_calculator import (
    calculate_fill_percentage,
    get_bin_status
)

from python_simulation.alert_system import check_alert

from python_simulation.report_generator import (
    generate_charts,
    generate_dashboard_image
)

csv_file = "data/waste_data.csv"

records = []

for i in range(20):

    timestamp, distance = generate_sensor_data()

    fill_percentage = calculate_fill_percentage(distance)

    status = get_bin_status(fill_percentage)

    alert = check_alert(fill_percentage)

    records.append([
        timestamp,
        distance,
        fill_percentage,
        status,
        alert
    ])

    print(
        timestamp,
        distance,
        fill_percentage,
        status,
        alert
    )

df = pd.DataFrame(
    records,
    columns=[
        "Timestamp",
        "Distance_cm",
        "Fill_Percentage",
        "Status",
        "Alert"
    ]
)

df.to_csv(csv_file, index=False)

generate_charts(csv_file)

generate_dashboard_image(csv_file)

print("\nProject Execution Completed Successfully!")

print("\nGenerated Files:")

print("data/waste_data.csv")
print("images/dashboard_output.png")
print("images/fill_level_trend_chart.png")
print("images/bin_status_distribution.png")
print("images/alert_status_chart.png")