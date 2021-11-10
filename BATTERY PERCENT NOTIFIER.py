import psutil
from plyer import notification
import time


def conversion(sec):
    sec_value = sec % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 60
    min_value = sec_value // 60
    sec_value %= 60
    return hour_value, min_value


while True:
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        print('Power mode(On battery)')
    else:
        print('Power mode(plugged in)')
    h, m = conversion(battery.secsleft)
    notification.notify(title="Battery Percentage",
                        message=f'{h}Hr {m}Min {battery.percent}% remaining',
                        timeout=10)
    time.sleep(600 * 600)
