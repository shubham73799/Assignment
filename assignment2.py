import psutil
import time

threshold = 80  # percent

print("Monitoring CPU usage...")

while True:
    try:
        usage = psutil.cpu_percent(interval=1)

        if usage > threshold:
            print("Alert! CPU usage is high:", usage, "%")

    except KeyboardInterrupt:
        print("\nStopped by user.")
        break

    except Exception as e:
        print("Error:", e)
