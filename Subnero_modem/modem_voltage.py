# assumes that unetpy is installed (pip install unetpy)
from unetpy import *
from modem_param import param as p
import time

t = 1

# Open a socket to the modem
sock = UnetSocket(p.IP, p.PORT)
modem = sock.getGateway()

phy = modem.agentForService(Services.PHYSICAL)

# Get voltage data every t seconds
while True:
    value = phy.voltage
    # Print the collected data with 2 decimal precision
    print('Voltage: %0.2f' % value)
    time.sleep(t)
