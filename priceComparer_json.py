import requests
import time
import os

#not used for reference if needed later
#myUrl = urllib.request.urlopen("http://www.ows.newegg.com/Products.egg/N82E16823129045/Specification")
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
		myUrl = requests.get("http://www.ows.newegg.com/Products.egg/N82E16823129045")
		pageJson = myUrl.json()

		#{} is for default value instead of null
		nameDesc = pageJson.get("Basic",{}).get("Title", {}).strip()
		price = pageJson.get("Basic",{}).get("FinalPrice")

		f.write(productId + "," + price.replace(",", "") + "," + time.strftime("%d/%m/%Y") + "," + nameDesc.replace(",", "|") + "\n")

		print("Name: " + nameDesc)
		print("Price: " + price)
		time.sleep(3)
	except Exception as e: 
		print(e)
#		pass

f.close()