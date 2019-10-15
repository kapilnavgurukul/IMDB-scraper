from pprint import pprint
from task1 import data
from task8 import scrape_movie_details
from task12 import  scrape_movie_cast

url=data[0]["url"]
def details_with_cast(url):
    movie_details=scrape_movie_details(url)
    cast=scrape_movie_cast(url)
    movie_details["cast"]=cast
    return movie_details

# pprint(details_with_cast(url))