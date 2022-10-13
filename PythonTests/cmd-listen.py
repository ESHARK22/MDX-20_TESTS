
# Connect to the serial port 6 with hardware flow control, for roland mdx-20

import serial as ser
import time

COM_PORT = 'COM4'
# Open serial port with hardware flow control
ser = ser.Serial(\
                 port=COM_PORT,
                 baudrate=9600,
                 bytesize=ser.EIGHTBITS,
                 parity=ser.PARITY_NONE,
                 stopbits=ser.STOPBITS_ONE,
                 xonxoff=False,
                 rtscts=True,
                 dsrdtr=False,
                 inter_byte_timeout=None,
                 exclusive=None
                 )


# Read the serial port
while True:
    print(ser.readline().decode())
    time.sleep(0.2)

