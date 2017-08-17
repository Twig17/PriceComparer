import os
import time

import requests
import Product

from database.ManageStorage import ManageStorage as storage
import database.StorageFactory as factory


class RetrieveData(object):
    def retrieveData():
        # not used for reference if needed later
        # myUrl = urllib.request.urlopen("http://www.ows.newegg.com/Products.egg/N82E16823129045/Specification")
        myProductIdList = ["N82E16814137142", "N82E16823129045"]

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

                thisProduct.id = productId
                thisProduct.name = nameDesc
                thisProduct.price = price
                # save product info to dataSource
                storageType.writeProduct(thisProduct)
                print("Name: " + nameDesc)
                print("Price: " + price)
                time.sleep(2)
            except Exception as e:
                print(e)
        storageType.closeConnection()

    if __name__ == '__main__':
        retrieveData()
