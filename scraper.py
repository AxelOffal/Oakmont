import requests
from bs4 import BeautifulSoup
#pretty print is used mostly to format results and make reading through html content easier and clearer
from pprint import pprint
#testing requests_html, not working just yet
from requests_html import HTMLSession

#not working method
#gets the html information of a dynamic site
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
