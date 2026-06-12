import pandas as pd
import matplotlib.pyplot as plt


def generate_charts(csv_file):

    df = pd.read_csv(csv_file)

    # Fill Level Trend Chart
    plt.figure(figsize=(8, 5))

    plt.plot(
        df["Fill_Percentage"],
        marker="o",
        linewidth=2
    )

    plt.title("Fill Level Trend")
    plt.xlabel("Reading Number")
    plt.ylabel("Fill Percentage (%)")
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "images/fill_level_trend_chart.png"
    )

    plt.close()

    # Bin Status Distribution Pie Chart
    status_counts = df["Status"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        status_counts,
        labels=status_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Bin Status Distribution")

    plt.tight_layout()

    plt.savefig(
        "images/bin_status_distribution.png"
    )

    plt.close()

    # Alert Status Distribution Pie Chart
    alert_counts = df["Alert"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        alert_counts,
        labels=alert_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Alert Status Distribution")

    plt.tight_layout()

    plt.savefig(
        "images/alert_status_chart.png"
    )

    plt.close()


def generate_dashboard_image(csv_file):

    df = pd.read_csv(csv_file)

    latest = df.iloc[-1]

    fig, ax = plt.subplots(figsize=(8, 4))

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