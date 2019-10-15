import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
from task13 import details_with_cast

movie_list=[]
for url1 in data:
    url=url1["url"]
    main_data=details_with_cast(url)
    movie_list.append(main_data)
# print(movie_list)

def analyse_co_actors(movie_list):
	co_actors={}
	for i in movie_list:
		id_=i["cast"][0]["imdb_id"]
		if id_ not in co_actors:
			co_actors[id_]={}
			co_actors[id_]["name"]=i["cast"][0]["name"]
			co_actors[id_]["frequent_co_actors"]=[]
		for j in i["cast"][1:6]:
			flag=True
			if len(co_actors[id_]["frequent_co_actors"])>0:
				for z in co_actors[id_]["frequent_co_actors"]:
					if z["imdb_id"]==j["imdb_id"]:
						z["num_movie"]+=1
						flag=False
			if flag :
				a={}
				a["imdb_id"]=j["imdb_id"]
				a["name"]=j["name"]
				a["num_movie"]=1
			co_actors[id_]["frequent_co_actors"].append(a)

	return co_actors
# pprint (analyse_co_actors(movie_list))