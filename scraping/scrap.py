import requests
from bs4 import BeautifulSoup

html_page = requests.get("https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv")

# print(html_page.text)

soup=BeautifulSoup(html_page.text,"lxml")
# print(soup)

header=soup.find('h1')
# print(header.text)


td_tag=soup.find("td",{'class':'titleColumn'})
# print(td_tag.text)

anker=td_tag.find("a")
# print(anker.text)

tr_tag=soup.find("tbody",{'class':'lister-list'})
# print(tr_tag.text)