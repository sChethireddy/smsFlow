'''
Created on 13-Oct-2022

@author: saipr
'''
import inspect
import logging


class Logs:
    
    
    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler("C:/Users/saipr/eclipse-workspace/smsFinal6/Logs/logfile.log")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        return logger