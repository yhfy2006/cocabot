#!/usr/bin/python
__author__ = 'vincentnewpro'

import os
import base64
from listener import listen
#import TokenManager
from TokenManager import *

class AudioManager:

    def __init__(self):
        self.tokenManager = TokenManager()
        self.audioFileName = "demo.wav"

    def record(self):
        listen(True,0)

    def getAudioLengh(self):
        if os.path.isfile(self.audioFileName):
            with open("demo.wav", "rb") as audio_file:
                encoded_string = base64.b64encode(audio_file.read())
                return encoded_string
        else:
            return ''

    def getAudioBase64(self):
        if os.path.isfile(self.audioFileName):
            b = os.path.getsize("demo.wav")
            return b
        else:
            return 0




if __name__ == '__main__':
    #print("please speak a word into the microphone")
    #token = TokenManager()
    manger = AudioManager()
    print(manger.getAudioLengh())
    print (manger.getAudioBase64())
    #print("done - result written to demo.wav")