from task8 import scrape_movie_details
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data

movie_list=[]
for i in data:
    url=i["url"]
    a=scrape_movie_details(url)
    movie_list.append(a)

def analyse_language_and_directors(movie_list):
	director_dict={}
	for i in movie_list:
		for directors in i["director"]:
			if directors not in director_dict:
				director_dict[directors]={}
			for j in i["Language"]:
				if j not in director_dict[directors]:
					director_dict[directors][j]=1
				else:
					director_dict[directors][j]+=1
	return director_dict

pprint(analyse_language_and_directors(movie_list))