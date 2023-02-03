'''
Created on 03-Oct-2022

@author: saipr
'''

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SpotmanLive():

    drop_down = "(//*[contains(text(),'arrow_drop_down')])[1]"
    garage = "//*[@autofocus='autofocus']"
    garage_path = "(//div[@role='option']//div[@class='v-list-item__title'])"

    def __init__(self,driver):
        
        self.driver = driver
        
    def selectGarage(self,garage_name):
        
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH ,self.drop_down))).click()
                
        self.driver.find_element("xpath",self.garage).send_keys(garage_name)
        
        self.driver.implicitly_wait(20)
        
        self.driver.find_element("xpath",self.garage_path).click()
