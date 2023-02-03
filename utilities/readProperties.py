'''
Created on 06-Oct-2022

@author: saipr
'''

import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/saipr/eclipse-workspace/smsFinal6/Configurations/config.ini")

class ReadConfig():
    
    @staticmethod
    def getURL():
        url=config.get('login info','baseURL')
        return url
    
    @staticmethod
    def getUserName():
        email=config.get('login info','username')
        return email
    
    @staticmethod
    def getPassword():
        password=config.get('login info','password')
        return password