from bs4 import BeautifulSoup
import requests,datetime
from pprint import pprint

y=0
next1=2
while y<next1:
	url="https://torrentgalaxy.org/torrents.php?parent_cat=&sort=id&order=desc&page="+str(y)
	url_data=requests.get(url).text

	soup=BeautifulSoup(url_data,"html.parser")
	main_div=soup.find("div",class_="tgxtable")
	all_div=main_div.find_all("div",class_="tgxtablerow")

	for h in all_div :
		dic={}
		type_div=h.find("div",{"class":"tgxtablecell shrink","id":"rounded"})
		typ=type_div.find("a").get_text().strip("\xa0")

		name_div=h.find("div",{"class":"tgxtablecell","id":"rounded","style":True})
		name=name_div.a.get_text()

		hash_div=h.find("div",{"class":"tgxtablecell","id":"rounded","style":"text-align:center;width:52px;padding-bottom:0px;padding-top:5px;"})
		find_a=hash_div.find_all("a")
		href=find_a[1]["href"]
		hesh=""
		for i in href[20:]:
			if "&" not in i:
				hesh+=i
			else:
				break

		size_div=h.find("div",{"class":"tgxtablecell","id":"rounded","style":"text-align:right;"})
		size=size_div.find("span",class_="badge badge-secondary").text

		sheet_div=h.find("span",{"title":"Seeders/Leechers"})
		sheet=sheet_div.find("font",{"color":"green"}).text

		date_div=h.find_all("div",{"class":"tgxtablecell","id":"rounded","style":"text-align:right;"})
		date=(date_div[1].text)
		if "ago" in date:
			current_time=datetime.datetime.now()
			a=date_div[1].small.get_text()
			int_=""
			for i in date:
				if i in ("0123456789"):
					int_+=i
			int_=int(int_)

			if a=="Min" or a=="Mins":
				date=current_time-(datetime.timedelta(minutes=int_))
				date=date.strftime("%d/%m/%y")
			elif a=="Hr" or a=="Hrs":
				date=current_time-(datetime.timedelta(hours=int_))
				date=date.strftime("%d/%m/%y")
		else:
			date=date[0:9]
		dic["name"]=name
		dic["hash"]=hesh
		dic["sheet"]=sheet
		dic["date"]=date
		dic["size"]=size
		pprint (dic)
	next_button=soup.find_all("li",class_="page-item")
	next2=(next_button[-2]).a.get_text()
	next1=int(next2)
	y+=1
