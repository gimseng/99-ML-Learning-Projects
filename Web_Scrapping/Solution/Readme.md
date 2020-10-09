There are 4 jupyter files available there in the solution . You just have to go one by one in order and you will get all the things.

## 1.Introduction_to_bs4_and_requests

- You need to install Beautifulsoup library first
- !pip install beautifulsoup4
- Introction to Beautifulsoup Explained
- How to parse and html form using Soup
- How to copy a web page onto local machine using requests
- requests is in-built library in python

## 2.Scrap_Snapdeal

- Crawling Snapdeal Website
- For a specific keyword , I am crawling keyowrd images over number of pages
- for example - url = "snapdeal.com/search?keyword=mobile"
- In the above url i searched for mobile and i will download all the phone images into output folder
- and we can run this program for more keywords at a time over number of pages 

## 3.projects_goodreads

### Project Overview

In this projects we will crawl goodreads website . We will fetch information like author,quotes,tags etc.And we will make a dataframe for this and after all we will analyse it's content .

### Description
- Crawling Goodreads website
- Goodreads is a good example website to scrap 
- Lets take a example 
- url_format = "https://www.goodreads.com/{}?page={}"
- replace first parameter for tags and 2nd parameters for number of pages
- Featched Information for the keywords over a number of pages
- Created a database of each quotes

## 4.EDA_Goodreads
- Analysed Goodreads Dataframe
- Tag column had inappropriate value 
- Handled Tag Column
- Checked for creating column of each tag category but that was not possible since there are total of 1606 category.
- Checked for missing using Heatmap





