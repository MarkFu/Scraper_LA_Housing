CREATE TABLE ScraperDB.temptbl LIKE ScraperDB.tbl_LA_Rental_Listing;
INSERT INTO ScraperDB.temptbl
SELECT * FROM ScraperDB.tbl_LA_Rental_Listing
GROUP BY Title;
DROP TABLE ScraperDB.tbl_LA_Rental_Listing;
ALTER TABLE ScraperDB.temptbl RENAME TO ScraperDB.tbl_LA_Rental_Listing;