import psutil
import time
import tkinter as tk

CUSTOM_PERCENTAGE = 30  # Can be adjusted to display alerts at different battery percentages
CUSTOM_SLEEP = 5  # Can be adjusted to shorten or lengthen the amount of minutes between alerts

def check_battery():
    # Defines variables for the battery percentage and charging status
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged

    # Displays an alert if the battery percentage is less than a user-defined value
    if percent < CUSTOM_PERCENTAGE and not charging:
        alert_window = tk.Tk()
        alert_window.title("Battery Alert!")
        alert_window.geometry("500x500")
        alert_label = tk.Label(alert_window, text=f"Battery is at {percent}%!\n Please plug in your laptop now!")
        alert_label.pack()
        alert_window.mainloop()

while True:
    check_battery()
    time.sleep(CUSTOM_SLEEP * 60)  # Converts the user-defined sleep time into seconds