import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
def grup_by_decade():
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
pprint (grup_by_decade())