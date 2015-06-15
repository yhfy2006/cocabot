__author__ = 'vincentnewpro'
import abc

class CocoService(object):
    #__metaclass__ = abc.ABCMeta
    processedData = {}

    @abc.abstractmethod
    def loadService(self,processedData):
        #print('data:'+processedData)
        self.processedData = processedData

    @abc.abstractmethod
    def printData(self):
        print self.processedData;

    @abc.abstractmethod
    def execute(self):
        return True