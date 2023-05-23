# SUMS-Tools
A collection of tools useful for running, maintaining, developing and other things related to the SUMS programme.
# Atlas_calibration
A collection of files useful when calibrating or verifying the validity of calibrated data
## lib
Module with both libraries relevant for the Atlas Scientific sensors.
## C/DO_logger.py
Both essentially work the same, they get the reading from the sensor and logs them to a file fastest sample time is T = 0.6 sec.
## ALL_logger.py
works like both C/DO loggers only here the fastes sample time is T = 1.2 sec.
# Subnero_modem
A collection of files with tools or functionality with the Subnero modem.

## modem_param
A module with some parameters for the modem that is connected:
 - IP
 - PORT
## logger.py
Script for listening and logging all data that is recieved.
## modem_sleep.py
Semi working script for putting the modem to sleep, only problem is that the script is setting a sleep schedule form now untill forever. This schedule is remembered between powerlosses and can only (in our experiance) be turned off in the browser interface.
## modem_volatage.py
There was an attempt to collect Voltage data from the modem but this was scrapped as the data collected from the PSM was more accurate.
## rx.py
Simple script for receiving data with the UnetScket API.
## tx.py
Simple script for sending some data with the UnetScket API.
