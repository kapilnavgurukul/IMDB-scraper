import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data

def scrape_movie_details(url):
    file_name=""
    for _id in url[27:]:
        if "/" not in _id:
            file_name+=_id
        else:
            file_name+=".json"
            break

    if os.path.isfile("json_files/"+file_name):
        with open("json_files/"+file_name,"r") as file:
            movie_details=json.load(file)
            return movie_details
    else:
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
 
            # here i find country and language and runtime
        county_lang_div=soup.find("div",attrs={"class":"article","id":"titleDetails"})
        country_div=county_lang_div.find_all(class_="txt-block")
        language=[]
        for i in country_div:
            try:
                a=(i.find("h4")).text
                # for country
                if a=="Country:":
                    country=(i.a.text)

                # for language	
                elif "Language:" in a:
                    language_div=(i.find_all("a"))
                    for j in language_div:
                        language.append(j.text)
            except AttributeError:
                continue
        
        # for runtime
        runtime_div=soup.find("div",class_="title_wrapper")
        time_div=runtime_div.find("time").text.strip().split()
        time=0
        for t in time_div:
            if "h" in t:
                hr=int(t[0:-1])
                time+=hr*60
            else:
                minut=int(t[0:-3])
                time+=minut

        # here i find poster url
        poster="https://www.imdb.com"+soup.find("div",class_="poster").find("a").get("href")

        # here i add all data in a dictenory
        movie_details["name"]=name.strip()
        movie_details["runtime"]=time
        movie_details["gener"]=movie_gener
        movie_details["bio"]=bio
        movie_details["director"]=director_name
        movie_details["Language"]=language
        movie_details["Country"]=country

        with open("json_files/"+file_name,"w") as file:
            json.dump(data,file)
        with open("json_files/"+file_name,"r") as file:
            movie_details=json.load(file)
            return movie_details

# for url1 in data:
#     url=url1["url"]
#     print(scrape_movie_details(url))