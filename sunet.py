#!/usr/bin/python

import numpy as np
import wave
import struct

frequency=1000
num_samples=4800

sampling_rate=48000.0
amplitude=16000
file="piano2.wave"
sine_wave=[np.sin(2*np.pi*frequency*x/sampling_rate)for x in range(num_samples)]
#wav_file=wave.open(file,'w')
for (k=0; k<BUFFER_LEN; k++){
	buffer[k]=sin(gain*2*pi*f/fs*k);}
    for(j=0;j<10000;j++){
	frames=snd_pcm_writei(handle, buffer, BUFFER_LEN);
