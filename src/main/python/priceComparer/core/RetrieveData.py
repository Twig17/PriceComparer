import time

import requests

import Product
import database.StorageFactory as factory
import websitesOnboard.WebsiteFactory as webFactory
import schedule


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
                thisProduct.productId = productId
                aWebsite = webFactory.chooseStorageType()
                thisProduct = aWebsite.getDataProduct(thisProduct)

                # save product info to dataSource
                storageType.writeProduct(thisProduct)

                # print values now for testing purposes
                print("Name: " + thisProduct.name)
                print("Price: " + thisProduct.price['Final'])
                print("Model: " + thisProduct.model)
                print("Original: " + thisProduct.price['Original'])
                print("Rebate: " + thisProduct.price['Rebate'])
                print("UrlLink: " + thisProduct.imageUrl)
                time.sleep(2)
            except Exception as e:
                print(e)
        storageType.closeConnection()

    if __name__ == '__main__':
        schedule.every(1).minutes.do(retrieveData)
        while 1:
            schedule.run_pending()
            time.sleep(1)
