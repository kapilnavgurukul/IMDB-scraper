# task 5
import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
from task4 import scrape_movie_details

def get_movie_list_details(top_movie):
	movie_details_list=[]
	for i in top_movie:
		url=i["url"]
		a=scrape_movie_details(url)
		movie_details_list.append(a)
	return movie_details_list

movie_details=(get_movie_list_details(data[0:10]))