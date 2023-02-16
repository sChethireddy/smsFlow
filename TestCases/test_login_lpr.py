'''
Created on 03-Oct-2022

@author: saipr
'''

from pageObjects.login import Spotman
from pageObjects.live import SpotmanLive
from pageObjects.bookingID import bookingLink
from pageObjects.paymentPage import addCard
from pageObjects.Entry import smsCheckin
from pageObjects.Exit import smsCheckOut
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logs
import time
from cardEmail import Email



class Test_Login():
    
    loginURL = ReadConfig.getURL()
    userEmail = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    
    log = Logs.getLogger()
    
    
    cardNumber = "4111 1111 1111 1111"
    expiryDate = "032023"
    Cvv = "123"
    zipCode = "20137"
    email = Email.gen_random_string(5)+"@gmail.com"
    
    lprUrl = "https://pinaboxapi-uat.divrt.co/api/v1/lpr"
    
    smsUrl = "https://pinaboxapi-uat.divrt.co/receive_sms"
    
    
    def test_lprCheckin(self):      #lpr checkin for a guest user
        
        
        lprIn = smsCheckin()
        
        lpr_response = lprIn.sendEntryRequest('.\\Testdata\\'+'lprIn.json',self.lprUrl)
        
        print(lpr_response.json()['message'])
        
        assert lpr_response.json()['status']==True
    
    def test_Entry(self,userEntry):             #sms checkin for a guest user
        
        
        self.log.info("*********API CHECKIN********")
        
        smsIN = smsCheckin()
        
        smsEntry = smsIN.sendEntryRequest(userEntry, self.smsUrl)
        
        
        global bookingId
        
        bookingId = smsEntry.json()['refno']
        
                
        if (bookingId):
            
            self.log.info("Entry Successful")
            
        else:
            
            self.log.error("User unable to checkin")
    
    def test_Spotman(self,setup,garageName):        #spotman actions
        
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.garage = garageName
        
        self.log.info("Login to Spotman")
        
        self.log1=Spotman(self.driver)
        
        self.log1.Login(self.userEmail,self.password)
        
        time.sleep(2)
            
        self.log.info("Login successful")
        
        self.driver.save_screenshot('.\\Images\\'+'Login.png')
        
        
        self.log.info("SELECT GARAGE")

        self.live1 = SpotmanLive(self.driver)
        self.live1.selectGarage(self.garage)
        time.sleep(2)
        self.log.info("Live page of garage")
        self.driver.save_screenshot('.\\Images\\'+'Garage.png')
        
        self.log.info("CLICK BOOKINGID")
        
        self.link = bookingLink(self.driver)
        self.link.clickSearch(bookingId)
        time.sleep(5)
        self.driver.save_screenshot('.\\Images\\'+'BookingId.png')
       
        self.link.refreshButton()
        
        time.sleep(2)
       
        self.link.clickLink()
        
        self.log.info("Clicked on BookingID")

        time.sleep(3)
        
        self.log.info("ENTER CARD DETAILS")
        
        self.card = addCard(self.driver)
        time.sleep(2)
        self.card.clickAddCard()
        time.sleep(1)
        self.card.enterCardDetails(self.cardNumber, self.expiryDate, self.Cvv, self.zipCode, self.email)
        self.log.info("Card Details Entered")
        time.sleep(3)
        self.driver.save_screenshot('.\\Images\\'+'CardDetails.png')
        self.card.clickAddPayment()
        self.log.info("Card Added")
        time.sleep(5)
        self.driver.save_screenshot('.\\Images\\'+'ExitPage.png')
        time.sleep(5)
        self.driver.close()
        self.driver.quit()
        
    
    def test_Exit(self,userExit):       #guest checkout using sms api
            
            
        self.log.info("API CHECKOUT")
            
        self.smsOut = smsCheckOut()
            
        booking_id_exit = self.smsOut.sendExitRequest(userExit)
            
        if(booking_id_exit):
                
            self.log.info("Exit Success")
                
        else:
            
            self.log.error("Exit Failure")
            
                
        
        