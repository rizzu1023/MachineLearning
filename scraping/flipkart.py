from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
import requests

my_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT&as-searchtext=iphone"

html_page = requests.get(my_url)
# print(html_page.text)

soup = BeautifulSoup(html_page.text,'lxml')
# print(soup)

containers = soup.findAll("div",{'class':'bhgxx2 col-12-12'})

# print(len(containers))

# print(soup.prettify(containers[0])).encode('utf-8')
print(soup.prettify().encode('utf-8'))



