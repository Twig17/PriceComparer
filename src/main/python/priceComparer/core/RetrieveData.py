import time

import requests

import Product
import database.StorageFactory as factory


class RetrieveData(object):
    def retrieveData():
        # not used for reference if needed later
        # myUrl = urllib.request.urlopen("http://www.ows.newegg.com/Products.egg/N82E16823129045/Specification")
        myProductIdList = ["N82E16814137142", "N82E16823129045","N82E16822107279"]

        # check if file exists to add to or create new file
        storageType = factory.chooseStorageType()
        storageType.setup()

        # loop through all product ids to get info price info
        for productId in myProductIdList:
            try:
                thisProduct = Product
                # open a connection
                myUrl = requests.get("http://www.ows.newegg.com/Products.egg/%s" % productId)
                pageJson = myUrl.json()

                # {} is for default value instead of null
                nameDesc = pageJson.get("Basic", {}).get("Title")
                price = pageJson.get("Basic", {}).get("FinalPrice")
                model = pageJson.get("Additional", {}).get("Model")
                originalPrice = pageJson.get("Basic", {}).get("OriginalPrice")
                rebate = pageJson.get("Basic", {}).get("RebateText")

                thisProduct.productId = productId
                thisProduct.name = nameDesc
                thisProduct.model = model
                allPrices = {}
                allPrices['Original'] = originalPrice
                allPrices['Rebate'] = rebate
                allPrices['Final'] = price
                thisProduct.price = allPrices
                # save product info to dataSource
                storageType.writeProduct(thisProduct)

                # print values now for testing purposes
                print("Name: " + nameDesc)
                print("Price: " + price)
                print("Model: " + model)
                print("Original: " + originalPrice)
                print("Rebate: " + rebate)
                time.sleep(2)
            except Exception as e:
                print(e)
        storageType.closeConnection()

    if __name__ == '__main__':
        retrieveData()
