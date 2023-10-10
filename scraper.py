from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#get the options for the chrome driver
options = webdriver.ChromeOptions()
#get the headless value and set it to True
options.headless = True
#define the driver as a chrome webdriver with the appropriate options and the service set as a chrome driver.
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
#if there is not an appropriate chrome driver defined for the driver above, the
#Service(ChromeDriverManager().install()) method will create one for use

def getHTML(url, headless = True):
    #if headless is turned off redefine the driver with the headless feature turned off
    if not headless:
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    
    #get the html information from the inputed url and load it with chrome
    driver.get(url)
    #wait for a small amount of time to let the site load
    driver.implicitly_wait(0.5)
    time.sleep(5)
    #exit chrome
    driver.quit
    #return the driver data
    return driver

#takes a json object result as a string and turns it back into its respective dictionary/list for use
def interpretJson(json):
    #evaluate what the json object should be and transform it into the given data type
    json = eval(json)
    return json
