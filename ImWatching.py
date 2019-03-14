import cv2
import numpy as np
import pyaudio
import audioop

# constants
ACTIVATEDB = 40.0

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
    db = toDB(in_data)
    if db > ACTIVATEDB:
        targetAndShoot()

# converts the data to db
def toDB(in_data):
    # Convert data from string
    audio_data = np.fromstring(in_data, np.int16)
    # Root mean's square of audio data
    rms = audioop.rms(audio_data, len(audio_data))
    # Convert to decible
    db = 20 * np.log10(rms)
    return db

def targetAndShoot():
    print "shooting"