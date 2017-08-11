from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import os

myUrl = 'https://www.newegg.com/Product/Product.aspx?Item=N82E16823129045'

myUrlNoId = 'https://www.newegg.com/Product/Product.aspx?Item='
myProductIdList = ["N82E16814137142", "N82E16823129045"]

#check if file exists to add to or create new file
filename = "productInfo.csv"
if os.path.exists(filename):
	f = open(filename, 'a')
else:
	f = open(filename, 'w')
	headers = "ProductId,Price,Date,Name\n"
	f.write(headers)

#loop through all product ids to get info price info
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

		price = pageSoup.body.select_one("div[id=container]").select_one('div[class="v660 background_F6F0E2"] > div').select_one("meta[itemprop=price]")["content"]

		f.write(productId + "," + price.replace(",", "") + "," + time.strftime("%d/%m/%Y") + "," + nameDesc.replace(",", "|") + "\n")

		print("Name: " + nameDesc)
		print("Price: " + price)
		time.sleep(5)
	except:
		pass

f.close()