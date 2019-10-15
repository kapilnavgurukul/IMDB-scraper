import requests,os,json,time,random
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import data
def grup_by_year():
    by_year={}
    for i in data:
        if i["year"] not in by_year:
            by_year[i["year"]]=[]
            by_year[i["year"]].append(i)
        else:
            by_year[i["year"]].append(i)
    return by_year
by_year=(grup_by_year())