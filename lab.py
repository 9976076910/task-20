

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import requests
url = "https://labour.gov.in/sites/default/files/ar_2022_23_english.pdf"


from selenium.webdriver import ActionChains




class Hover:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       self.driver.get(self.url)
       sleep(5)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()


   def findElementByXPath(self, xpath):
       return self.driver.find_element(by=By.XPATH, value=xpath)


   def goToLabour(self):

           self.boot()
           practiceElement = self.findElementByXPath('//*[@id="nav"]/li[7]/a')
           # move the mouse to the middle of the element
           self.action.move_to_element(practiceElement).perform()
           sleep(5)

           self.findElementByXPath('//*[@id="nav"]/li[7]/ul/li[3]/a').click()
           print("https://labour.gov.in/sites/default/files/ar_2022_23_english.pdf")
           response = requests.get(url)
           sleep(5)


   def goToMedia(self):

               self.boot()
               practiceElement1 = self.findElementByXPath('//*[@id="nav"]/li[10]/a')
               # move the mouse to the middle of the element
               self.action.move_to_element(practiceElement1).perform()
               sleep(5)
               self.findElementByXPath('//*[@id="nav"]/li[10]/a').click()
               print(self.driver.current_url)
               sleep(5)
               self.quit()
hover = Hover("https://labour.gov.in/")
hover.goToLabour()
hover.goToMedia()