import scraper
from selenium.webdriver.common.by import By
import re 

#get the consumer price index and monthly index from the reserve bank of Australia site
def getRBAInflation():
    #get the html data for the RBA website
    url = "https://www.rba.gov.au/inflation-overview.html"
    data = scraper.getHTML(url)
    #find all entries with a class of 'landing-page-chart-statistic-value'
    data = data.find_elements(By.CLASS_NAME, "landing-page-chart-statistic-value")
    #set each value found to the respective named values below
    ConsumerPriceIndex = data[0].text
    MonthlyPriceIndex = data[1].text
    #return them
    return ConsumerPriceIndex, MonthlyPriceIndex

#get the monthly costs of living for a family of 4 and 1 from the expatistan site
def getExpantism():
    #get the html data for the expatistan website
    url = "https://www.expatistan.com/cost-of-living/country/australia"
    data = scraper.getHTML(url)
    #find all elements which use a span tag and have the class 'price'
    data = data.find_elements(By.XPATH,'//span[@class="price"]')
    #set each respective monthly cost to the result and return
    monthlyCostFamilyOfFour = data[0].text
    monthlyCostSinglePerson = data[1].text
    return monthlyCostFamilyOfFour, monthlyCostSinglePerson

#//li/label

#gets the lowest and highest fuel price across australia
def getFuelPrice():
    #get the html data for australian fuel prices
    url = "https://fuelprice.io/"
    data = scraper.getHTML(url)
    #find all elements that are a label contained within a li tag
    data = data.find_elements(By.XPATH,'//li/label')
    #set the results to there respective values
    lowestprice = data[0].text
    highestprice = data[1].text
    #return the results
    return lowestprice, highestprice 

#woolies/coles lists
#wonderwhite bread, royal gala apples 

#get the woolies price for bananas
def getWooliesBread():
    #link to the woolies page on bananas
    url = "https://www.woolworths.com.au/shop/productdetails/263669/wonder-white-bread-vitamins-minerals-sandwich"
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    #find the element in the page with the class name 'shelfProductTile-cupPrice'
    data = data.find_element(By.CLASS_NAME, "shelfProductTile-cupPrice")
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    return data 

#get the woolies price for bananas
def getWooliesApples():
    #link to the woolies page on bananas
    url = "https://www.woolworths.com.au/shop/productdetails/155003/apple-royal-gala"
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    #find the element in the page with the class name 'shelfProductTile-cupPrice'
    data = data.find_element(By.CLASS_NAME, "shelfProductTile-cupPrice")
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    return data 

#get the woolies price for bananas
def getWooliesBananas():
    #link to the woolies page on bananas
    url = "https://www.woolworths.com.au/shop/productdetails/133211/cavendish-bananas"
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    #find the element in the page with the class name 'shelfProductTile-cupPrice'
    data = data.find_element(By.CLASS_NAME, "shelfProductTile-cupPrice").text
    #return the internal HTML attribute of that element
    #data = data.get_attribute('innerHTML')
    return data 

#get the woolies price for bananas
def getWooliesChicken():
    #link to the woolies page on bananas
    url = "https://www.woolworths.com.au/shop/productdetails/25734/woolworths-rspca-approved-chicken-breast-fillet"
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    #find the element in the page with the class name 'shelfProductTile-cupPrice'
    data = data.find_element(By.CLASS_NAME, "shelfProductTile-cupPrice")
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    return data 

#get the woolies price for bananas
def getColesBread():
    #link to the woolies page on bananas
    url = "https://www.coles.com.au/product/wonder-white-bread-+-vitamins-and-mineral-700g-5795130"
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    #find the element in the page with the class name 'shelfProductTile-cupPrice'
    data = data.find_element(By.CLASS_NAME, "price__calculation_method")
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    return data 

def interpretPrice(inputs):
    return float(re.search('[0-9]\.[0-9][0-9]', inputs).group())

def interpretWeight(inputs):
    return (re.search(' ([0-9]+.*)', inputs).group(1))

print(getWooliesApples(),"\n", getWooliesBananas(),"\n", getWooliesBread(),"\n", getWooliesChicken())