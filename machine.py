import random
import time

# Simulated machine list
machines = {
    "Machine_1": {"location": "Assembly"},
    "Machine_2": {"location": "Welding"},
    "Machine_3": {"location": "Painting"},
}

# Health assessment logic
def assess_health(temp, vibration):
    if temp > 80 or vibration > 5:
        return "CRITICAL"
    elif temp > 60 or vibration > 3:
        return "WARNING"
    else:
        return "NORMAL"

# Main monitoring loop
def monitor_machines():
    while True:
        print("\n--- Machine Health Report ---")
        for name in machines:
            # Simulated sensor data
            temperature = round(random.uniform(40, 100), 2)  # degrees Celsius
            vibration = round(random.uniform(0, 7), 2)        # arbitrary units

            # Health status
            health = assess_health(temperature, vibration)

            # Print report
            print(f"{name} | Temp: {temperature}°C | Vibration: {vibration} | Status: {health}")
        
        time.sleep(3)  # Wait 3 seconds before next check

# Run the monitoring
monitor_machines()
