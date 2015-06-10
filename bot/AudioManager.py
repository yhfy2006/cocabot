#!/usr/bin/python
__author__ = 'vincentnewpro'

import os
import base64
from listener import *
import json
from TokenManager import *
import requests
from cocoListener import CocoListener

class AudioManager:

    def __init__(self):
        self.tokenManager = TokenManager()
        self.audioFileName = "demo.wav"
        self.listener = CocoListener()

    def record(self):
        self.listener.record_to_file(self.audioFileName)

    def getAudioBase64(self):
        if os.path.isfile(self.audioFileName):
            with open("demo.wav", "rb") as audio_file:
                encoded_string = base64.b64encode(audio_file.read())
                return encoded_string
        else:
            return ''

    def getAudioLength(self):
        if os.path.isfile(self.audioFileName):
            b = os.path.getsize("demo.wav")
            return b
        else:
            return 0

    def sendAudio(self):
        meta = {}
        meta['format'] = 'wav'
        meta['rate'] = 16000
        meta['channel'] = 1
        meta['token'] = self.tokenManager.getToken();
        meta['cuid'] = 'testCguid'
        meta['len'] = self.getAudioLength()
        meta['speech'] = self.getAudioBase64()
        payload = json.dumps(meta,sort_keys=True,indent=4, separators=(',', ': '))
        print(payload)
        headers = {'Content-Type':'application/json','Content-length':len(payload)}
        r = requests.post('http://vop.baidu.com/server_api', data=payload,headers = headers)
        print(r.json())




if __name__ == '__main__':
    #print("please speak a word into the microphone")
    #token = TokenManager()
    manger = AudioManager()
    manger.record()
    manger.sendAudio()
    #print(manger.getAudioLengh())
    #print (manger.getAudioBase64())
    #print("done - result written to demo.wav")