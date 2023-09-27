from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
#options.headless = True
DRIVER_PATH = "C:\\Users\\aj\\OneDrive\\code\\year 3\\IT Project2\\driver\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

def getHTML(url):
    #get the html information from the inputed url and load it with chrome
    driver.get(url)
    #wait for a small amount of time to let the site load
    driver.implicitly_wait(0.5)
    time.sleep(4)
    #exit chrome
    driver.quit
    #return the driver data
    return driver

#takes a json object result as a string and turns it back into its respective dictionary/list for use
def interpretJson(json):
    #evaluate what the json object should be and transform it into the given data type
    json = eval(json)
    return json
