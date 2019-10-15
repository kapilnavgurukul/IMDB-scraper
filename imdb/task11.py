from task8 import scrape_movie_details
from pprint import pprint
from task1 import data

movie_list=[]
for i in data:
    url=i["url"]
    a=scrape_movie_details(url)
    movie_list.append(a)

def analyse_movies_genre(movie_list):
	gener_dict={}
	for j in movie_list:
		for i in j["gener"]:
			if i not in gener_dict:
				gener_dict[i]=1
			else:
				gener_dict[i]+=1
	return gener_dict
pprint(analyse_movies_genre(movie_list))