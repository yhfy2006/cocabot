__author__ = 'vincentnewpro'
import subprocess

class QuickPlayTTS(object):

    @staticmethod
    def quickPlay(str):
        cmd = 'python pyUtils/GoogleTTS.py -l zh-CN -o Resource/tmp.mp3 -s '+ u' '.join(str).encode('utf-8').strip()
        print cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line,
        p.wait()

        p = subprocess.Popen('afplay Resource/tmp.mp3', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line,
        p.wait()