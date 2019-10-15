from task1 import data
from task13 import details_with_cast
from pprint import pprint

movie_list=[]
for url1 in data:
    url=url1["url"]
    main_data=details_with_cast(url)
    movie_list.append(main_data)
# print(movie_list)

def actors_count(movie_list):    # count actor movie 
	count_dict={}
	for i in movie_list:
		for i in i["cast"]:
			if i["imdb_id"] not in count_dict:
				count_dict[i["imdb_id"]]={}
				count_dict[i["imdb_id"]]["name"]=i["name"]
				count_dict[i["imdb_id"]]["num_movies"]=1
			else:
				count_dict[i["imdb_id"]]["num_movies"]+=1
	return count_dict
# pprint (actors_count(movie_list))
