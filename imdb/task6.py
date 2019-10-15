import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
from task5 import movie_details
def analyse_movies_language(movie_list):
	language_count={}
	for i in movie_list:
		for j in i["Language"]:
			if j not in language_count:
				language_count[j]=1
			else:
				language_count[j]+=1
	return language_count

pprint (analyse_movies_language(movie_details))