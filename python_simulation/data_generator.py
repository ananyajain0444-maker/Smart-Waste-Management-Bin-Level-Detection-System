import random
from datetime import datetime

BIN_HEIGHT = 100  # cm

def generate_sensor_data():
    distance = random.randint(5, 100)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, distance