import requests
from bs4 import BeautifulSoup
#pretty print is used mostly to format results and make reading through html content easier and clearer
from pprint import pprint
from requests_html import HTMLSession
import re

#gets the html information of a link
#method takes the link and header information used to represent a browser when requesting links, by default it is set to represent a firefox user
def getHtmlSession(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}):
    session = HTMLSession()
    #request for the sites html information from our given link
    data = session.get(link)
    data.html.render(sleep=5)

    html = data.html.text
    #html = BeautifulSoup(data.html.html, 'html.parser')
    
    return html


#gets the html information of a link
#method takes the link and header information used to represent a browser when requesting links, by default it is set to represent a firefox user
def getHtml(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}):
    #request for the sites html information from our given link
    data = requests.get(link, headers=headers, stream=True, timeout=10).content
    #pass our html information using BeautifulSoup so that it can be filtered through
    html = BeautifulSoup(data, 'html.parser')
    return html

#takes a json object result as a string and turns it back into its respective dictionary/list for use
def interpretJson(json):
    #evaluate what the json object should be and transform it into the given data type
    json = eval(json)
    return json

#gets the price of Bannanas from coles
def getColes():
    #get the html info from coles
    html = getHtml('https://www.coles.com.au/product/fresh-bananas-approx.-180g-409499')
    #find the script information from the page with a type of application/ld+json
    data = html.find('script', type='application/ld+json')
    #take that data and interpret it into a proper json format and get the information within offers and price
    data = data.contents
    result = interpretJson(data[0])
    result = result['offers'][0]['price']
    #return the price
    return result

def getRBAInflation():
    #get html info
    html = getHtml('https://www.rba.gov.au/inflation-overview.html')
    #find all p tag elements with the class 'landing-page-chart-statistic-value'
    data = html.findAll('p', class_="landing-page-chart-statistic-value")
    
    #set consumerIndex and monthlyIndicator
    consumerIndex = data[0].text
    monthlyIndicator = data[1].text

    #get the digit values for each value
    consumerIndex = re.search("\d+\.\d+", consumerIndex).group()
    monthlyIndicator = re.search("\d+\.\d+", monthlyIndicator).group()
    #return the consumer price index, and monthly indicator
    return consumerIndex, monthlyIndicator

htmls = "https://www.rba.gov.au/inflation-overview.html"

pprint(getRBAInflation())