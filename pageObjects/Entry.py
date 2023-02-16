'''
Created on 03-Oct-2022

@author: saipr
'''
import requests
import json

#from readData import Data

class smsCheckin():
    
    def sendEntryRequest(self,fileName,apiEntry):
    
        
        with open(fileName) as input_data:
           
            data=json.load(input_data)
        
        for i in data["userdetails"]:
            
            api_response = requests.post(url=apiEntry,data=i)
            
            return api_response