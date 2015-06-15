import pyaudio
import math
import struct
import wave

class Listener:

    #Assuming Energy threshold upper than 30 dB
    THRESHOLD = 30
    SHORT_NORMALIZE = (1.0/32768.0)
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    SWIDTH = 2
    MAX_SECONDS = 5
    TIMEOUTSIGNAL=(RATE / CHUNK * MAX_SECONDS)
    SILENCE = True
    FileNameTmp = 'demo.wav'
    TIME=0
    ALLCHUNCKDATA =[]

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format = self.FORMAT,channels = self.CHANNELS,rate =self.RATE,input = True, output = True,frames_per_buffer = self.CHUNK)
        self.listen(self.SILENCE,self.TIME)

    def GetStream(self,chunk):
        return self.stream.read(chunk)



    def rms(self,frame):
        count = len(frame)/self.SWIDTH
        format = "%dh"%(count)
        shorts = struct.unpack( format, frame )

        sum_squares = 0.0
        for sample in shorts:
            n = sample * self.SHORT_NORMALIZE
            sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5);

        return rms * 1000



    def WriteSpeech(self,WriteData):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        wf = wave.open(self.FileNameTmp, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(WriteData)
        wf.close()



    def KeepRecord(self,TimeoutSignal, LastBlock):


        self.ALLCHUNCKDATA.append(LastBlock)
        for i in range(0, TimeoutSignal):
            try:
                data = self.GetStream(self.CHUNK)
            except:
                continue
                #I chage here (new Ident)
            self.ALLCHUNCKDATA.append(data)

        print "end record after timeout";
        data = ''.join(self.ALLCHUNCKDATA)
        print "write to File";
        self.WriteSpeech(data)
        self.SILENCE = True
        self.TIME=0
        #listen(silence,Time)

    def listen(self,silence,Time):
        print "waiting for Speech"
        while silence:

            try:

                input = self.GetStream(self.CHUNK)

            except:

                continue


            rms_value = self.rms(input)

            if (rms_value > self.THRESHOLD):

                silence=False

                LastBlock=input

                print "hello ederwander I'm Recording...."
                self.KeepRecord(self.TIMEOUTSIGNAL, LastBlock)

            Time = Time + 1

            if (Time > self.TIMEOUTSIGNAL):
                print "Time Out No Speech Detected"
                sys.exit()






if __name__ == "__main__":
    listener = listener()
    listener.start()