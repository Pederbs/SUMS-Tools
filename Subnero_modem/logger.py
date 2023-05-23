from unetpy import UnetSocket
from modem_param import param as p
import csv
import datetime

sock = UnetSocket(p.IP, p.PORT)

file = 'SUMS_logger.csv'

header = 'Received_time,Modem_ID,Time,Depth,Voltage,Oxygen,Salinity,Temerature'

with open(file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([header])

while True:
    print('Listening...')
    rx = sock.receive()
    
    now_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(now_time, 'from node', rx.from_, ':', bytearray(rx.data).decode())
    streng = now_time + ',' + str(rx.from_) + ','
    streng += bytearray(rx.data).decode()

    with open(file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([streng])