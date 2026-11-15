import time
import random
json

def telemetry_generator():
    print("Starting hardware telemetry simulation... Press Ctrl+C to stop.")
    try:
        while True:
            sensor_wave = 50 + 35 * (time.time() % 10) + random.uniform(-2, 2)
            motor_rpm = max(0, min(100, 70 + 20 * random.gauss(0, 1)))
            battery_lvl = 84.5
            power_draw = 14.2 + random.uniform(-1.0, 1.0)

            payload = {
                "timestamp": time.time(),
                "oscilloscope": round(sensor_wave, 2),
                "rpm": round(motor_rpm, 1),
                "battery": round(battery_lvl, 1),
                "power": round(power_draw, 2)
            }
            print(f"TX -> {json.dumps(payload)}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nTelemetry stream stopped.")

if __name__ == "__main__":
    telemetry_generator()