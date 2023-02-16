'''
Created on 03-Oct-2022

@author: saipr
'''

from selenium.webdriver.common.by import By


class addCard():
    
    addCC = "//span[normalize-space()='ADD CREDIT CARD']"
    addPayment = "//span[normalize-space()='ADD PAYMENT']"
    
    def __init__(self,driver):
        
        self.driver = driver
    
    def clickAddCard(self):
        
        self.driver.find_element("xpath",self.addCC).click()
        
    
    def enterCardDetails(self,cardNumber,expiryDate,Cvv,zipCode,email):
        
        self.driver.switch_to.frame("heartland-frame-cardNumber")
        self.driver.find_element(By.NAME,"cardNumber").send_keys(cardNumber)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("heartland-frame-cardExpiration")
        self.driver.find_element(By.NAME,"cardExpiration").send_keys(expiryDate)


        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("heartland-frame-cardCvv")
        self.driver.find_element(By.NAME,"cardCvv").send_keys(Cvv)

        self.driver.switch_to.default_content()

        self.driver.find_element(By.ID,"postal_code").send_keys(zipCode)

        self.driver.find_element(By.ID,"email_address").send_keys(email)
        
        
    def clickAddPayment(self):
        
        self.driver.find_element("xpath",self.addPayment).click()
        