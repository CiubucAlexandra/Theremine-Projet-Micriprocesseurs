#!/usr/bin/python
import pygame, numpy, pygame.sndarray

sampleRate=44100
pygame.mixer.pre_init(sampleRate, -16, 1)
#pygame.mixer.init()
pygame.init()

arr=numpy.array([4096*numpy.sin(2.0*numpy.pi*440*x/sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
sound=pygame.sndarray.make_sound(arr)

sound.play(-1)
pygame.time.delay(10000)
sound.stop
