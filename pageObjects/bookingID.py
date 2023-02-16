'''
Created on 03-Oct-2022

@author: saipr
'''




class bookingLink():
    
    search_box = "(//input[@type='text'])[8]"
    
    book_xpath = "(//a[@target='_blank'])[1]"
    
    refresh_xpath = "//i[contains(.,'refresh')]"
    
    
    def __init__(self,driver):
        
        self.driver = driver
        
    def clickSearch(self,bookingIdVal):
        
        
        self.driver.find_element("xpath",self.search_box).send_keys(bookingIdVal)
        
        self.driver.implicitly_wait(5)
        
        
    def clickLink(self):
        
        self.driver.find_element("xpath",self.book_xpath).click()
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        
    def refreshButton(self):
        
        self.driver.find_element("xpath",self.refresh_xpath).click()
        
        