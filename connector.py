import pandas as pd
from sqlalchemy import create_engine
import scraper
import pymysql

str_url_master = "https://losangeles.craigslist.org/d/housing/search/hhh"
num_page_range = 10

conn = create_engine('mysql+pymysql://LARentalScraper:LAscraper2018@scraperdb.cdfom3jx46ff.us-west-1.rds.amazonaws.com:3306/ScraperDB?charset=utf8', encoding = 'utf-8')

df = scraper.scraper(str_url_master, num_page_range)

df.to_sql('tbl_LA_Rental_Listing', con = conn, if_exists = 'append', index = False)