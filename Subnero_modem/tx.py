from unetpy import UnetSocket
from modem_param import param as p

# Variable for who shall receive the message
# 0 = everyone
receiver = 0

sock = UnetSocket(p.IP, p.PORT) 
sock.send('Hello Underwater!', receiver)
sock.close()
