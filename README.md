# BATTERY-PERCENT-NOTIFIER
In this project, we are going to display the battery notification and the time left for the battery to drain out using the battery capacity value.

Libraries used in this project
- psutil
- plyer

Installing these libraries can be done using the following commands
- pip install psutil
- pip install plyer

Note: These commands should be installed in the command prompts.
If you are using jupyter, run these commands on anaconda prompt before running the code in jupyter notebook

EXPLANATION:

After importing required modules from the libraries, the following functions are used in the code

`psutil.sensors_battery()`

This method returns the value of percentage of battery in the sysytem


`battery.power_plugged`

Checks if the system is on charging mode or not


`time.sleep()`

It is a sleep function which is used to add delay in the execution of the program


`notification.notify()`

It is used to display the notification
