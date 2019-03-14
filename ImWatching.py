import cv2
import numpy as np
import pyaudio

#TODO Figure out capture device of camera
vCap = cv2.VideoCapture(0)

# TODO Add audio capture
pa = pyaudio.PyAudio()

stream = pa.open(format = pyaudio.paFloat32,
                 channels = 1,
                 rate = 44100,
                 input = True,
                 frames_per_buffer = 1024,
                 stream_callback = checkForActivate)

while stream.is_active():
    print "listening"



def checkForActivate(in_data, # recorded data if input=True
                     frame_count, # number of frames
                     time_info, #dictionary
                     status_flags): #pyaudio callback flags
    print "Is Callback"