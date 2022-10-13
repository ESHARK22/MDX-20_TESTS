#echo ;;^^IN;!RC0;!MC1;!PZ0,40;^^PU**xConv**,**yConv**;V3;Z**xConv**,**yConv**,**zConv**;!MC0; > com3

# Connect to the serial port 6 with hardware flow control, for roland mdx-20

import serial as ser
import time

xMove = 2   *4
yMove = 0   *4  
zMove = 0   *4
COM_PORT = 'COM3'
Extend = True

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


def move_command(x, y, z):
    xConv = x * 4
    yConv = y * 4
    zConv = z * 4
    command = \
        "^^IN;!RC0;!MC1;!PZ0,40;^^PU" \
        + str(xConv) \
        + "," + str(yConv) \
        + ";V3;Z" \
        + str(xConv) \
        + "," + str(yConv) \
        + "," + str(zConv) \
        + ";!MC0;"

    if Extend == True:
        command += ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"

    return command

start_x = 2
start_y = 0
start_z = 0

Home = 0
while True:

    if Home == 5:
        print("Sendding to home!")
        command = move_command(5, 5, 0)
        ser.write(command.encode())
        print(">> Done!")
        Home = 0
    else:
        print("Attempting to move to: " + str(start_x) + ", " + str(start_y) + ", " + str(start_z))

        command = move_command(int(start_x), start_y, start_z)
        ser.write(command.encode())
        print(">>Done!")

        if start_x < 0:
            start_x = start_x * -1
        elif start_x > 0:
            start_x = start_x * -1
    
    Home += 1
    time.sleep(2)



