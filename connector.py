import pandas as pd
import pymysql
import scraper

host = "scraperdb.cdfom3jx46ff.us-west-1.rds.amazonaws.com"
port = 3306
dbname = "ScraperDB"
user = "LARentalScraper"
password = "LAscraper2018"

str_url_master = "https://losangeles.craigslist.org/d/housing/search/hhh"
num_page_range = 10

conn = pymysql.connect(host, 
	user = user,
	port = port,
	passwd = password, 
	db = dbname)

df = scraper.scraper(str_url_master, num_page_range)

df.to_sql('tbl_LA_Rental_Listing', conn, if_exists = 'append', index = False)