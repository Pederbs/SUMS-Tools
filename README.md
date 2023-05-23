# SUMS-Tools
A collection of tools useful for running, maintaining, developing and other things related to the SUMS programme.



# Atlas_loggers
A collection of files useful when calibrating or verifying the validity of calibrated data

For files spesific to calibrating Atlas Scientific sensors visit:
https://github.com/AtlasScientific/Raspberry-Pi-sample-code/tree/master
## lib
Module with both libraries relevant for the Atlas Scientific sensors.
## C/DO_logger.py
Both essentially work the same, they get the reading from the sensor and logs them to a file fastest sample time is T = 0.6 sec.
## ALL_logger.py
works like both C/DO loggers only here the fastes sample time is T = 1.2 sec.
## notes_calibration.md
A **VERY** informal notes file for when i tried to calibrate the Atlas sensors, I first tried in UART then I2C. I strongly recomend I2C.



# graycodeCompression
functions that allow conversion form float numbers to graycode of a given bit size.

- ``graycode_equivalent(num)``: This function takes an integer num and returns its corresponding Gray code equivalent, which is a binary numeral system where two consecutive values differ in only one digit.

- ``graycode(num, bits)``: This function takes an integer num and an integer bits, and returns the Gray code representation of num as a binary string of length bits. Note that this function only works for values of bits less than 10.

- ``compress(number, lowerlim, upperlim, bits, gain)``: This function takes a float number, a lower limit lowerlim, an upper limit upperlim, an integer bits, and a gain gain. It returns an integer that represents a compressed version of the original number. The output integer is determined by mapping the range between lowerlim and upperlim to a binary range of length bits, and then scaling that range by gain.

- ``gray_to_int(gray_code)``: This function takes a binary string gray_code in Gray code format and converts it to the corresponding integer value.

- ``unpack(number, lowerlim, upperlim, bits, gain)``: This function takes an integer number (presumably generated by the compress function), a lower limit lowerlim, an upper limit upperlim, an integer bits, and a gain gain. It returns the original uncompressed float value that was used to generate the input number.


# simulator_SUMS
Simulator for running SUMS code without sensors on devices that do not have i2c capabilities.



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



# unet-3.4.0
Files for simulating modems if none are accessable, note that Java version 8? is needed to run this. Good tutorials can be found on UnetStack web page:

Java 8?
https://stackoverflow.com/questions/75626405/error-while-trying-to-run-2-node-network-groovy-example

UnetStack handbook: (good tutorials and documentation)
https://unetstack.net/handbook/unet-handbook.html
