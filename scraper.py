import re, requests
from lxml import html
import bs4
import pandas as pd

str_url = "https://losangeles.craigslist.org/d/housing/search/hhh"

url = str_url
url_content = requests.get(url).content
soup = bs4.BeautifulSoup(url_content, "lxml")
list_posts = soup.findAll('p') # find all posts

list_all_p = list() # placeholder for scraped fields for all posts

for p in list_posts:
	str_hood = p.findAll('span', class_ = 'result-hood')
	if str_hood:
		str_hood = str_hood[0].text
	str_price = p.findAll('span', class_ = 'result-price')
	if str_price:
		str_price = str_price[0].text
	str_housing = p.findAll('span', class_ = 'housing')
	if str_housing:
		str_housing = str_housing[0].text
	str_date = p.findAll('time')
	if str_date:
		str_date = str_date[0].text
	str_title = p.findAll('a', class_ = 'result-title hdrlnk')
	if str_title:
		str_title = str_title[0].text
	list_all_p.append([str_title, str_date, str_price, str_hood, str_housing])

df_all_p = pd.DataFrame(list_all_p, columns = ['Title', 'Date', 'Price', 'Neighborhood', 'Housing'])

writer_temp = pd.ExcelWriter('temp.xlsx')
df_all_p.to_excel(writer_temp, 'full', index = False)
writer_temp.save()
writer_temp.close() 
exit()