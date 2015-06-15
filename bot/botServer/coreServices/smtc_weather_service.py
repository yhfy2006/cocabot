#!/usr/bin/python
# -*- coding: utf-8 -*-
from cocoService import CocoService
from bot.botServer.pyUtils.quickplayTTS import QuickPlayTTS

class Smtc_weather_service(CocoService):

    def execute(self):
        data = self.processedData
        results = data['data']['result']
        bestAnswer = results[0]
        ans = self.formAnswerString(bestAnswer)
        QuickPlayTTS.quickPlay(ans)


    def formAnswerString(self,ansDict):
        ans = ansDict['city']+','+ansDict['weather']+','+ ansDict['wind']+',气温'.decode('utf-8')+ansDict['tempRange']
        return  ans

testclass = Smtc_weather_service()
testclass.loadService('addd')