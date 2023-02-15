import psutil
import time
import tkinter as tk

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged
    if percent < 30 and not charging:
        alert_window = tk.Tk()
        alert_window.title("Battery Alert!")
        alert_window.geometry("500x500")
        alert_label = tk.Label(alert_window, text=f"Battery is at {percent}%!\n Please plug in your laptop now!")
        alert_label.pack()
        alert_window.mainloop()

while True:
    check_battery()
    time.sleep(300)  # 5 minutes in seconds