import pandas as pd
from sqlalchemy import create_engine
import scraper

str_url_master = "https://losangeles.craigslist.org/d/housing/search/hhh"
num_page_range = 10

conn = create_engine('mysql+mysqldb://LARentalScraper:LAscraper2018@scraperdb.cdfom3jx46ff.us-west-1.rds.amazonaws.com:3306/ScraperDB')

df = scraper.scraper(str_url_master, num_page_range)

df.io.sql.to_sql('tbl_LA_Rental_Listing', con = conn, if_exists = 'append', index = False)