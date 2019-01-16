#!/usr/bin/python

from __future__ import print_function
import time
from zx_sensor import ZxSensor
import pygame, numpy, pygame.sndarray

def gotoxy(x,y):
	print("%c[%d;%df" % (0x1B,y,x), end='')

sampleRate=44100
zx_sensor=ZxSensor(0x10)
pygame.mixer.pre_init(sampleRate, -16, 1)
pygame.init()
while(True):
#	sampleRate=44100
	if zx_sensor.position_available():
		z=zx_sensor.read_z()
		#x=zx_sensor.read_x()
		arr=numpy.array([4096*z*numpy.sin(2.0*numpy.pi*440*x/sampleRate)for x in range(0, sampleRate)]).astype(numpy.int16)
		sound=pygame.sndarray.make_sound(arr)
		sound.play(-1)
		pygame.time.delay(1000)
		#z_str="{0:03d} ".format(int(z))
		#print('\033[2J')
		#gotoxy(int(x/2),int(44-z/8))
		#print(z_str)
		sound.stop()
		#time.sleep(.07)
		

