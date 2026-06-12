import pandas as pd
import matplotlib.pyplot as plt


def generate_charts(csv_file):

    df = pd.read_csv(csv_file)

    # Fill Level Trend Chart
    plt.figure(figsize=(8, 5))
    plt.plot(
        df["Fill_Percentage"],
        marker="o"
    )

    plt.title("Fill Level Trend")
    plt.xlabel("Reading Number")
    plt.ylabel("Fill Percentage (%)")
    plt.grid(True)

    plt.savefig(
        "images/fill_level_trend_chart.png"
    )

    plt.close()

    # Bin Status Distribution Chart
    status_counts = df["Status"].value_counts()

    plt.figure(figsize=(6, 6))

    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Bin Status Distribution")

    plt.savefig(
        "images/bin_status_distribution.png"
    )

    plt.close()


def generate_dashboard_image(csv_file):

    df = pd.read_csv(csv_file)

    latest = df.iloc[-1]

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.axis("off")

    dashboard_text = (
        "SMART WASTE MANAGEMENT DASHBOARD\n\n"
        f"Distance : {latest['Distance_cm']} cm\n"
        f"Fill %   : {latest['Fill_Percentage']}%\n"
        f"Status   : {latest['Status']}\n"
        f"Alert    : {latest['Alert']}"
    )

    ax.text(
        0.05,
        0.5,
        dashboard_text,
        fontsize=12
    )

    plt.savefig(
        "images/dashboard_output.png"
    )

    plt.close()


def generate_report_image(csv_file):

    df = pd.read_csv(csv_file)

    fig, ax = plt.subplots(
        figsize=(10, 4)
    )

    ax.axis("off")

    table = ax.table(
        cellText=df.head(10).values,
        colLabels=df.columns,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)

    plt.savefig(
        "images/waste_monitoring_report.png"
    )

    plt.close()