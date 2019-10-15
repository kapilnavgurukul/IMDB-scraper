
import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup


def scrape_top_list():
    if os.path.exists("scrap_first.json"):
        with open("scrap_first.json","r") as file:
            data=json.load(file)
            return(data)
    data=[]
    url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
    soup=BeautifulSoup(url.text,"html.parser")
    position=[]
    z=[]
    dic={}
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
        data.append(dic.copy())
    with open("scrap_first.json","w") as file:
        json.dump(data,file)
    return data

data=scrape_top_list()
