import scraper
import re

#gets the price of Bannanas from coles
def getColes():
    #get the html info from coles using the getHtml method from the scraper module
    html = scraper.getHtml('https://www.coles.com.au/product/fresh-bananas-approx.-180g-409499')
    #find the script information from the page with a type of application/ld+json
    data = html.find('script', type='application/ld+json')
    #take that data and interpret it into a proper json format and get the information within offers and price
    data = data.contents
    #use the interpretJson method from scraper to get a nested list for use
    result = scraper.interpretJson(data[0])
    result = result['offers'][0]['price']
    #return the price
    return result

def getRBAInflation():
    #get html info from the RBA website
    html = scraper.getHtml('https://www.rba.gov.au/inflation-overview.html')
    #find all p tag elements with the class 'landing-page-chart-statistic-value'
    data = html.findAll('p', class_="landing-page-chart-statistic-value")
    
    #set consumerIndex and monthlyIndicator
    consumerIndex = data[0].text
    monthlyIndicator = data[1].text

    #get the consumerIndex and monthlyIndicator values
    consumerIndex = re.search("\d+\.\d+", consumerIndex).group()
    monthlyIndicator = re.search("\d+\.\d+", monthlyIndicator).group()
    #return the consumer price index, and monthly indicator
    return consumerIndex, monthlyIndicator

print(getRBAInflation())