'''
Created on 20-Oct-2022

@author: saipr
'''
import pandas as pd
import json

class userData:
    
    @staticmethod
    def getJsonData(fileName):
        
        
        #myJson=pd.read_json(fileName,lines=False,orient="records")
        
        return json.load(open(fileName))
    
    @staticmethod
    def getExitData(filename):
        
        myJson1=pd.read_json(filename,lines=False,orient="records")
        
        return myJson1