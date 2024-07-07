from bs4 import BeautifulSoup
import requests

url = "http://example.com"
response = requests.get(url)
#make html more readable with help from BeautifulSoup' , 'html.parse' is use for html only
HtmlParser = BeautifulSoup(response.content, "html.parser")
#print(HtmlParser)

#take title
title = HtmlParser.title.text
#find the first p in html
content = HtmlParser.find("p").text
#find all link href in html
links = [a['href'] for a in HtmlParser.find_all('a')]

print("title: "+ title)
print("content: "+ content)
print("link: " + links[0])