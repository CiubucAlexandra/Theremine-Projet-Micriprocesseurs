#!/usr/bin/env python

""" Basic example of retrieving the zx_sensor data, via the I2C interface of
a Rasberry Pi. Tested with Pi2. When run, prints 'x' & 'z' to console
"""


from __future__ import print_function
import time
# project
from zx_sensor import ZxSensor

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

# Initialise the ZxSensor device using the default address
zx_sensor = ZxSensor(0x10)

while (True):
    if zx_sensor.position_available():
        # display raw values:
        # print('x {0} z {1}'.format(zx_sensor.read_x(), zx_sensor.read_z()))

        # display z as console animation:
        z = zx_sensor.read_z()
        x = zx_sensor.read_x()
        z_str = "{0:03d} ".format(int(z))
        #line = "." * (int(z / 4) + 1)
        print('\033[2J')

        gotoxy(int(x/2), int(44-z/8))
        print(z_str)

        time.sleep(.07)
