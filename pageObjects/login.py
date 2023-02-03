'''
Created on 03-Oct-2022

@author: saipr
'''



class Spotman():
    
    
    email_xpath = "//*[@id='input-19']"
    password_xpath = "//*[@name='password']"
    login_xpath = "//*[contains(text(),'Log in')]"
    
    
    def __init__(self,driver):
        
        self.driver = driver
    
    
    def Login(self,userEmail,password):
        
        self.driver.find_element("xpath",self.email_xpath).send_keys(userEmail)
        self.driver.find_element("xpath",self.password_xpath).send_keys(password)
        self.driver.find_element("xpath",self.login_xpath).click()