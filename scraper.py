from selenium import webdriver
import time

options = webdriver.ChromeOptions()
#options.headless = True

driver = webdriver.Chrome(options=options)

def getHTML(url):
    #get the html information from the inputed url and load it with chrome
    driver.get(url)
    #wait for a small amount of time to let the site load
    time.sleep(10)
    #exit chrome
    driver.quit
    #return the driver data
    return driver

#takes a json object result as a string and turns it back into its respective dictionary/list for use
def interpretJson(json):
    #evaluate what the json object should be and transform it into the given data type
    json = eval(json)
    return json
