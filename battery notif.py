from pynotifier import Notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent
Notification("battery percentage", str(percent)+ "%percent remainig",duration=20).send()
