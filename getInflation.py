import scraper
from selenium.webdriver.common.by import By
import re 
from pprint import pprint

def interpretPrice(inputs):
    #remove all commas from any numbers 
    inputs = inputs.replace(',','')
    #find the number from inside of the given string
    result = float(re.search('[0-9]+(\.[0-9][0-9])?', inputs).group())
    #return the price result
    return result

def interpretWeight(inputs):
    #find the weight/distribution of items and return
    return (re.search(' ([0-9]+.*)', inputs).group(1))


#----------------
#get the consumer price index and monthly index from the reserve bank of Australia site
def getRBAInflation():
    #get the html data for the RBA website
    url = "https://www.rba.gov.au/inflation-overview.html"
    data = scraper.getHTML(url)

    #attempt to find elements in page
    try:
        #find all entries with a class of 'landing-page-chart-statistic-value'
        data = data.find_elements(By.CLASS_NAME, "landing-page-chart-statistic-value")
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #set each value found to the respective named values below 
    #additionally refine the values to be the proper price values
    ConsumerPriceIndex = interpretPrice(data[0].text)
    MonthlyPriceIndex = interpretPrice(data[1].text)
    #return them
    return ConsumerPriceIndex, MonthlyPriceIndex

#----------------
#get the monthly costs of living for a family of 4 and 1 from the expatistan site
def getExpantismMonthlyCost():
    #get the html data for the expatistan website
    url = "https://www.expatistan.com/cost-of-living/country/australia"
    data = scraper.getHTML(url)

    #attempt to find elements in page
    try:
        #find all elements which use a span tag and have the class 'price'
        data = data.find_elements(By.XPATH,'//span[@class="price"]')
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #set each respective monthly cost to the result and return
    monthlyCostFamilyOfFour = interpretPrice(data[0].text)
    monthlyCostSinglePerson = interpretPrice(data[1].text)
    return monthlyCostFamilyOfFour, monthlyCostSinglePerson

#comparison single-city
def getExpantismSectorPrices():
    #get the html data for the expatistan website
    url = "https://www.expatistan.com/cost-of-living/country/australia"
    data = scraper.getHTML(url)

    #attempt to find elements in page
    try:
        #find all elements within the table with the class name 'comparison single-city'
        data = data.find_elements(By.XPATH,'//table[@class="comparison single-city"]/tbody/tr')
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    
    #create a price dictionary
    prices = []
    #for each entry in our data
    for entry in data:

        #attempt to find sub element data
        try:
            #get all children of our entry
            entries = entry.find_elements(By.XPATH,'*')
        #if we can't find the element
        except:
            #raise a SubElementDataNotFound Exception
            raise Exception('SubElementDataNotFound')

        
        #if there are more than two children entries
        if len(entries) > 2:
            #set price to the value at index 2
            price = str(entries[2].text)
            #set the name to the values at index 1
            name = entries[1].text
            #add a dictionary entry to prices with the respective name and price
            prices.append([name, interpretPrice(price)])
    #return our sector prices
    return prices
#----------------
#currently broken, appears to be due to a change in the site which prevents scraping
"""
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
"""
#----------------  
#gets the price data of any valid product on the woolies site
def getWoolies(url):
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url, False)
    #attempt to find elements in page
    try:
        #find the element in the page with the class name 'shelfProductTile-cupPrice'
        data = data.find_element(By.CLASS_NAME, "shelfProductTile-cupPrice").text
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #takes out the price and the weight of the product
    data = interpretPrice(data), interpretWeight(data)
    #return the internal HTML attribute of that element
    return data 

#get the woolies price for bananas
def getWooliesBread():
    #link to the woolies page on bread
    url = "https://www.woolworths.com.au/shop/productdetails/263669/wonder-white-bread-vitamins-minerals-sandwich"
    #process with the getWoolies method to get the price data
    data = getWoolies(url)
    return data 

#get the woolies price for bananas
def getWooliesApples():
    #link to the woolies page on Apples
    url = "https://www.woolworths.com.au/shop/productdetails/155003/apple-royal-gala"
    #process with the getWoolies method to get the price data
    data = getWoolies(url)
    return data 

#get the woolies price for bananas
def getWooliesBananas():
    #link to the woolies page on bananas
    url = "https://www.woolworths.com.au/shop/productdetails/133211/cavendish-bananas"
    #process with the getWoolies method to get the price data
    data = getWoolies(url)
    return data 

#get the woolies price for chicken
def getWooliesChicken():
    #link to the woolies page on chicken breast fillet
    url = "https://www.woolworths.com.au/shop/productdetails/25734/woolworths-rspca-approved-chicken-breast-fillet"
    #process with the getWoolies method to get the price data
    data = getWoolies(url)
    return data 

def getColes(url):
    #get the html data for the page from the scraper module
    data = scraper.getHTML(url)
    return data 

#get the coles price for bread
def getColesBread():
    #link to the coles bread page
    url = "https://www.coles.com.au/product/wonder-white-bread-+-vitamins-and-mineral-700g-5795130"
    #process coles page with getColes method
    data = getColes(url)
    #attempt to find elements in page
    try:
        #find the element in the page with the class name 'price_calculation_method'
        data = data.find_element(By.CLASS_NAME, "price__calculation_method")
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    #takes out the price and the weight of the product
    data = interpretPrice(data), interpretWeight(data)
    return data 

#get the coles price for chicken breast fillet
def getColesChicken():
    #link to the coles chicken breast fillet page
    url = "https://www.coles.com.au/product/coles-rspca-approved-chicken-breast-fillets-large-pack-approx.-1.4kg-2263179"
    #process coles page with getColes method
    data = getColes(url)
    #attempt to find elements in page
    try:
        #find the element in the page with the class name 'price_calculation_method'
        data = data.find_element(By.CLASS_NAME, "price__calculation_method")
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    #takes out the price and the weight of the product
    data = interpretPrice(data), interpretWeight(data)
    return data 

#get the coles price for Apples
def getColesApples():
    #link to the coles Apples page
    url = "https://www.coles.com.au/product/coles-royal-gala-apples-loose-approx.-160g-each-5226000"
    #process coles page with getColes method
    data = getColes(url)
    #attempt to find elements in page
    try:
        #find the element in the page with the class name 'price_value'
        data = data.find_element(By.CLASS_NAME, "price__value")
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    #takes out the price per item saved as a tuple
    data = interpretPrice(data), '1EA'
    return data 

#get the coles price for bananas
def getColesBananas():
    #link to the coles bananas page
    url = "https://www.coles.com.au/product/fresh-bananas-approx.-180g-each-409499"
    #process coles page with getColes method
    data = getColes(url)
    #attempt to find elements in page
    try:
        #find the element in the page with the class name 'price_value'
        data = data.find_element(By.CLASS_NAME, "price__value")
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #return the internal HTML attribute of that element
    data = data.get_attribute('innerHTML')
    #takes out the price per item saved as a tuple
    data = interpretPrice(data), '1EA'
    return data 
#----------------
#get average Australian price for petroleum (car fuel)
def getAIPFuel():
    #Link for the australian insitute of Petroleum
    url = "http://www.aip.com.au/pricing/national-retail-petrol-prices"
    #use the scraper to get the html data
    data = scraper.getHTML(url)
    #attempt to find elements in page
    try:
        #get the table data of the National Australian average price
        data = data.find_element(By.XPATH,'//table/tbody/tr[3]/td[2]')
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #get the string value
    data = data.get_attribute('innerHTML')
    #Convert to a float
    data = float(data)
    #return the final data
    return data
#-----
#get the average index values representing housing prices
def getCoreLogic():
    #Link for CoreLogic Housing prices
    url = "https://www.corelogic.com.au/our-data/corelogic-indices"
    #use the scraper to get the html data
    data = scraper.getHTML(url)
    #attempt to find elements in page
    try:
        #get the table data of the National Australian Housing indexs
        data = data.find_elements(By.CLASS_NAME, 'graph-row')
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    
    #set a temporary list
    temp = []
    #for each row of data
    for i in data:

        #attempt to find sub elements
        try:
            #find all the columns inside of the row
            i = i.find_elements(By.TAG_NAME, 'div')
        #if we can't find the element
        except:
            #raise a SubElementDataNotFound Exception
            raise Exception('SubElementDataNotFound')

        #take the entries at 0 and 3 and append those as a tuple to temp
        temp.append((i[0].text,i[3].text))
    #replace temp with data
    data = temp
    #return the formated data
    return data

#get the price for a bottle of Jack daniels
def getAlcoholDaniels():
    url = "https://www.mybottleshop.au/jack-daniels-1907-white-label-heritage-bottle-700ml"
    data = scraper.getHTML(url)
    #attempt to find elements in page
    try:
        #get the item price
        data = data.find_element(By.CLASS_NAME,'price').text
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    #interpret the price data
    data = interpretPrice(data)
    #return the drink price
    return data
    
#get the pricec for an 18 case of asahi
def getAlcoholAsahi():
    url = "https://www.mybottleshop.au/asahi-super-dry-black-bottle-18x334ml-bottles"
    data = scraper.getHTML(url)
    #attempt to find elements in page
    try:
        #get the item price
        data = data.find_element(By.CLASS_NAME,'price').text
    #if we can't find the element
    except:
        #raise a DataNotFound Exception
        raise Exception('DataNotFound')
    #interpret the price data
    data = interpretPrice(data)
    #return the drink price
    return data

print(getAlcoholAsahi(), getAlcoholDaniels())
"""
list = [getAIPFuel(), getColesApples(), getColesChicken(), getExpantismSectorPrices()]
for i in list:
    print(i)
    """