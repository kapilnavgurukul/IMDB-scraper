import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup

url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(url.text,"html.parser")

# task 1
def scrape_top_list():
	psition=[]
	z=[]
	dic={}
	list1=[]
	div_data=soup.find('div',class_="lister")
	tbody_data=div_data.find("tbody",class_="lister-list")
	tr_data=tbody_data.find_all("tr")

	# here i find position
	for i in tr_data:
		position=i.find("td",class_="titleColumn").get_text().strip()
		# return (position)
		z=""
		for j in position:
			if j==".":
				break
			else:
				z+=j
		
		# here i find movie
		td=i.find("td",class_="titleColumn")
		movie=td.find("a").text

		# here i find year
		year=i.find("td",class_="titleColumn").span
		all_year=year.text[1:5]

		# here i find rating
		rat=i.find("td",class_="ratingColumn imdbRating")
		rating=rat.text.strip()

		# here i find url
		url=td.find("a").get("href")

		# here i add in a dictinory all data
		all_url="https://www.imdb.com"+url
		dic["position"]=z
		dic["movie"]=movie
		dic["year"]=all_year
		dic["rating"]=rating
		dic["url"]=all_url
		list1.append(dic.copy())
	return (list1)
# pprint (scrape_top_list())


# this function for year to movie     (task 2)
def grup_by_year():
	data=scrape_top_list()
	by_year={}
	for i in data:
		if i["year"] not in by_year:
			by_year[i["year"]]=[]
			by_year[i["year"]].append(i)
		else:
			by_year[i["year"]].append(i)
	return by_year
# pprint (grup_by_year())


# this function for decade     (task 3)
def grup_by_decade():
	data=scrape_top_list()[:10]
	decade={}
	for i in data:
		year=str(i["year"])
		key_year=year[0:3]+"0"
		if key_year not in decade:
			decade[key_year]=[]
			decade[key_year].append(i)
		else:
			decade[key_year].append(i)
	return decade
# pprint (grup_by_decade())


# task 4
def scrape_movie_details(url):

	# for task 8                         (8)
	file_name=""
	for _id in url[27:]:
		if "/" not in _id:
			file_name+=_id
		else:
			file_name+=".json"
			break

	text=None
	if os.path.exists(file_name):
		a=open(file_name,"r")
		text=a.read()
		text=json.loads(text)
		return text

	# # for task 9                            (9)
	# time.sleep(random.randint(1,4))

	# for task 4
	movie_details={}
	url_data=requests.get(url).text
	soup=BeautifulSoup(url_data,"html.parser")

	# here i find name of movie
	name_data=soup.find("div",class_="title_wrapper").h1.get_text()
	name=""
	for i in name_data.strip():
		if "(" not in i:
			name=name+i
		else:
			break
	# here i find runtime in  minit
	run_time=soup.find("div",class_="subtext").time.get_text().strip()
	runtime_hour=int(run_time[0])*60
	runtime_min=0
	if "min" in run_time:
		runtime_min=int(run_time[3:].strip("min"))+runtime_hour
	else:
		runtime_min=runtime_hour

	# here i find gener
	gener=soup.find("div",class_="subtext")
	gener_a=gener.find_all("a")
	gener_a.pop()
	movie_gener=[i.get_text() for i in gener_a ]

	# here i find movie bio
	bio=soup.find("div",class_="summary_text").text.strip()

	# here i find director name
	director_div=soup.find("div",class_="credit_summary_item")
	director=director_div.find_all("a")
	director_name=[i.get_text() for i in director]

	# here i find contry and language 
	extra_details=soup.find("div",attrs={"class":"article","id":"titleDetails"})
	list_of_divs=extra_details.find_all("div",class_="txt-block")
	for div in list_of_divs:
		tag_h4=div.find_all("h4")
		for i in tag_h4:
			if "Country" in i.text:
				tag_anchor=div.find_all("a")
				country="".join([j.get_text() for j in tag_anchor])
			elif "Language" in i.text:
				tag_anchor=div.find_all("a")
				language=[j.get_text() for j in tag_anchor]

	# here i find poster url
	poster="https://www.imdb.com"+soup.find("div",class_="poster").find("a").get("href")

	# here i add all data in a dictenory
	movie_details["name"]=name.strip()
	movie_details["runtime"]=runtime_min
	movie_details["gener"]=movie_gener
	movie_details["bio"]=bio
	movie_details["director"]=director_name
	movie_details["Language"]=language
	movie_details["Country"]=country

	# part of task 8 
	fi
	le1=open(file_name,"w")
	raw=json.dumps(movie_details)
	file1.write(raw)
	file1.close()
	
	return movie_details
# pprint (scrape_movie_details(scrape_top_list()[1]["url"]))


# task 5
def get_movie_list_details(top_movie):
	movie_details_list=[]
	for i in top_movie:
		url=i["url"]
		a=scrape_movie_details(url)
		movie_details_list.append(a)
	return movie_details_list
# pprint(get_movie_list_details(scrape_top_list()))

# task 6
def analyse_movies_language(movie_list):
	language_count={}
	for i in movie_list:
		for j in i["Language"]:
			if j not in language_count:
				language_count[j]=1
			else:
				language_count[j]+=1
	return language_count
# pprint (analyse_movies_language(get_movie_list_details(scrap_top_list())))

# task 7
def analyse_movies_directors(movie_list):
	director_count={}
	for i in movie_list:
		for j in i["director"]:
			if j not in director_count:
				director_count[j]=1
			else:
				director_count[j]+=1
	return director_count
# pprint(analyse_movies_directors(get_movie_list_details(scrap_top_list())))





# task 10
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
# pprint(analyse_language_and_directors(get_movie_list_details(scrap_top_list())))


# task 11
def analyse_movies_genre(movie_list):
	gener_dict={}
	for j in movie_list:
		for i in j["gener"]:
			if i not in gener_dict:
				gener_dict[i]=1
			else:
				gener_dict[i]+=1
	return gener_dict
# pprint (analyse_movies_genre(get_movie_list_details(scrap_top_list())))


# task 12
def scrape_movie_cast(movie_cast_url):

	# caching ke liye
	url_id=""
	for i in movie_cast_url[27:36]:
		url_id+=i
	id_name=url_id+"_cast.json"
	if os.path.exists(id_name):
		a=open(id_name,"r")
		a_data=a.read()
		return_list=json.loads(a_data)
		a.close()
		return return_list

	url_id=movie_cast_url[27:36]
	url_cast="https://www.imdb.com/title/"+url_id+"/fullcredits?ref_=tt_cl_sm#cast"
	url_data=requests.get(url_cast).text
	soup=BeautifulSoup(url_data,"html.parser")
	div=soup.find('div',attrs={"class":'header',"id":"fullcredits_content"})
	tbody=div.find("table",class_="cast_list")
	# print (tbody)
	trs=tbody.find_all("tr",class_=True)
	# print (trs)
	return_list=[]
	for tr in trs:
		dic={}
		tds=tr.find_all("td")
		td_a=tds[1].find("a")
		name=td_a.text.strip()
		href=td_a.get("href")
		id_=href[6:15]
		dic["imdb_id"]=id_
		dic["name"]=name
		return_list.append(dic.copy())

	# caching k liye
	a=open(id_name,"w")
	a_data=json.dumps(return_list)
	a.write(a_data)
	a.close()

	return return_list
# pprint (scrape_movie_cast(scrape_top_list()[0]["url"]))



# task 13
def details_with_cast(url):
	a=scrape_movie_details(url)
	b=scrape_movie_cast(url)
	a["cast"]=b
	return a
# pprint (details_with_cast(scrape_top_list()[0]["url"]))

#  edit or get_movie_list_details
# top_movie=(scrape_top_list())
def get_movie_list_details_modified(top_movie):
	movie_details_list=[]
	for i in top_movie:
		url=i["url"]
		a=scrape_movie_details(url)
		b=scrape_movie_cast(url)
		a["cast"]=b
		movie_details_list.append(a)
	return movie_details_list
# pprint (get_movie_list_details_modified(top_movie[:10]))


# task 14
def analyse_co_actors(movie_list):   #main actor and co actor till 50
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
						print ("kapil")
						flag=False
			if flag :
				a={}
				a["imdb_id"]=j["imdb_id"]
				a["name"]=j["name"]
				a["num_movie"]=1
			co_actors[id_]["frequent_co_actors"].append(a)

	return co_actors
# pprint (analyse_co_actors(get_movie_list_details_modified(scrape_top_list())))

# task 15
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
# pprint (actors_count(get_movie_list_details_modified(scrape_top_list())))
