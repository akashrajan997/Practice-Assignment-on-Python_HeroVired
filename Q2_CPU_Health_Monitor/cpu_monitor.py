import psutil
import time

def monitor_cpu(threshold=80):
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu}%")
            if cpu > threshold:
                print("ALERT: CPU usage exceeded 80%!")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_cpu()
