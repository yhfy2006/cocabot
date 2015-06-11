from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cococmd/<cmd>')
def cocoCommand(cmd):
    return cmd;

@app.route('/tts/<txt>')
def tts(txt):
    cmd = 'python pyUtils/GoogleTTS.py -l zh-CN -o Resource/tmp.mp3 -s '+ u' '.join(txt).encode('utf-8').strip()
    print cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    p.wait()

    p = subprocess.Popen('afplay Resource/tmp.mp3', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    p.wait()
    #subprocess.call(['python','GoogleTTS.py','-l','zh-CN','tmp.mp3','-s',txt])
    return 'done'


if __name__ == '__main__':
    app.debug = True
    app.run()
