'''
Created on 03-Oct-2022

@author: saipr
'''

import requests
import json

class smsCheckOut():


    def sendExitRequest(self,userOut):
        
        with open(userOut) as input_data:
           
            data=json.load(input_data)
        
        for i in data["userdetails"]:
            
            resp = requests.post("https://pinaboxapi-dev.divrt.co/receive_sms",data=i)
            
            print(resp.json())
            
            booking_id_exit = resp.json()['refno']
        
            print("Boooking ID for entry is " " "+resp.json()['refno'])
        
        return booking_id_exit
            