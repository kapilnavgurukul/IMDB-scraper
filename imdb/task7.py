import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task5 import movie_details
def analyse_movies_directors(movie_list):
	director_count={}
	for i in movie_list:
		for j in i["director"]:
			if j not in director_count:
				director_count[j]=1
			else:
				director_count[j]+=1
	return director_count

pprint(analyse_movies_directors(movie_details))