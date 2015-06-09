#!/usr/bin/python
__author__ = 'vincentnewpro'
import requests
import os
import json
import time

class TokenManager:
    def __init__(self):
        self.apiKey = "tbLjh3cu2YBxkGeBN5cAxkLH"
        self.secret = "bec1577c2a2545cf258523055d7ea9eb"
        self.tokenFileName = "token.json"


    def getTokenJson(self):
        payload = {'grant_type': 'client_credentials', 'client_id':self.apiKey ,"client_secret":self.secret}
        r = requests.post('https://openapi.baidu.com/oauth/2.0/token', data=payload)
        with open(self.tokenFileName,'w') as tokefile:
            jsonData = r.json()
            editableJsonData = {key:value for key, value in jsonData.items()}
            currentTime = int(round(time.time()))
            editableJsonData["setTime"]=currentTime
            json.dump(editableJsonData,tokefile);
            return editableJsonData

    def getTokenFromAPI(self):
        jsonData = self.getTokenJson();
        return jsonData['access_token']

    def getToken(self):
        if not os.path.isfile(self.tokenFileName):
            return self.getTokenFromAPI()
        else:
            with open(self.tokenFileName) as jsonDataFile:
                jsonData = json.load(jsonDataFile)
                current = int(round(time.time()))
                setDate = jsonData['setTime']
                expiredtime = jsonData['expires_in']
                if setDate+expiredtime < current :
                    return self.getTokenFromAPI()
                else:
                    return jsonData['access_token']



#tokenManager = TokenManager()
#print(tokenManager.getToken())

