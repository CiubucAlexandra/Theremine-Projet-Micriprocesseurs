#! /usr/bin/python
import pygame
from pygame import *

import math
import numpy

size=(1366, 720)

bits=16

pygame.mixer.pre_init(44100, -bits, 2)
pygame.init()
#_display_surf=pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
duration=1.0
frequency_l=440
frequency_r=550

sample_rate=44100
n_samples =int(round(duration*sample_rate))

buf=numpy.zeros((n_samples, 2), dtype=numpy.int16)
max_sample=2**(bits-1)-1

for s in range(n_samples):
    t=float(s)/sample_rate

buf[s][0]=int(round(max_sample*math.sin(2*math.pi*frequency_l*t)))
buf[s][1]=int(round(max_sample*0.5*math.sin(2*math.pi*frequency_r*t)))

sound=pygame.sndarray.make_sound(buf)
sound.play(loops=-1)

_running=True
#while _running:
 #     for event in pygame.event.get():
#	 if event.type ==pygame.QUIT:
#		_running=False
#		break
pygame.quit()
