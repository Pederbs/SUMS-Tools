from unetpy import UnetSocket
from modem_param import param as p

sock = UnetSocket(p.IP, p.PORT) 
# Set how long the modem should listen for, 
# if not defined the modem will listen forever
# sock.setTimeout(5*1000) # Listen for 5 sec
rx = sock.receive()
print('from node', rx.from_, ':', bytearray(rx.data).decode())
sock.close()
