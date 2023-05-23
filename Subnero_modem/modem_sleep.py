from unetpy import *
from modem_param import param as p


# Open a socket to the modem
sock = UnetSocket(p.IP, p.PORT)
modem = sock.getGateway()

phy = modem.agentForService(Services.PHYSICAL)

# Sets a sleep schedule from now --> forever
# This schedule have to be deleted from the browser interface 
# in the sleep schedule tab
print(phy << AddScheduledSleepReq())