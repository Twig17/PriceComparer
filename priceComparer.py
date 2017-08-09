from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import os

myUrl = 'https://www.newegg.com/Product/Product.aspx?Item=N82E16823129045'

myUrlNoId = 'https://www.newegg.com/Product/Product.aspx?Item='
myProductIdList = ["N82E16814137142", "N82E16823129045"]

filename = "productInfo.csv"
if os.path.exists(filename):
	f = open(filename, 'a')
else:
	f = open(filename, 'w')
	headers = "ProductId,Price,Date,Name\n"
	f.write(headers)


for productId in myProductIdList:
	try:
		# open a connection
		uClient = uReq(myUrlNoId+productId)
		pageHtml = uClient.read()
		uClient.close()

		#get the html from the url
		pageSoup = soup(pageHtml, "html.parser")

		nameDescContainer = pageSoup.body.findAll("h1", {"id":"grpDescrip_h"})
		nameDesc = nameDescContainer[0].text.strip()

		price = pageSoup.body.findAll("div", {"id":"container"})[0].findAll("div", {"class":"v660 background_F6F0E2"})[0].div.find("meta", {"itemprop":"price"})["content"]

		print("Name: " + nameDesc)
		print("Price: " + price)
		time.sleep(5)

		f.write(productId + "," + price.replace(",", "") + "," + time.strftime("%d/%m/%Y") + "," + nameDesc.replace(",", "|") + "\n")
	except AttributeError:
		pass

f.close()