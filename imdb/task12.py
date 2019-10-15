import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
def scrape_movie_cast(movie_cast_url):
	# caching ke liye
	url_id=""
	for i in movie_cast_url[27:36]:
		url_id+=i
	id_name=url_id+"_cast.json"
	if os.path.isfile("cast_json/"+id_name):
		a=open("cast_json/"+id_name,"r")
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
	a=open("cast_json/"+id_name,"w")
	a_data=json.dumps(return_list)
	a.write(a_data)
	a.close()
	return return_list

# pprint (scrape_movie_cast(data[0]["url"]))

