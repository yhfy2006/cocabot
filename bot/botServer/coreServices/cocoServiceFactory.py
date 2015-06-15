__author__ = 'vincentnewpro'
from smtc_weather_service import Smtc_weather_service
from cocoService import CocoService
class CocoServiceFactory:

    preloadServices = {}

    def __init__(self):
        self.preloadServices['weather'] = Smtc_weather_service()

    def invokeWithData(self,initialData):
        self.currentServiceData = initialData
        serviceName = initialData['service']
        srvInstance = self.preloadServices[serviceName]
        if isinstance(srvInstance, CocoService):
            srvInstance.loadService(initialData)
            srvInstance.execute()




    def parseData(self):
        pass
