import time

import requests

import Product
import database.StorageFactory as factory
import websitesOnboard.WebsiteFactory as webFactory
import schedule


class RetrieveData(object):
    def retrieveData():
        # check if file exists to add to or create new file
        storageType = factory.chooseStorageType()
        storageType.setup()

        myProductIdList = storageType.getAllProductIds()

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
                displayValues = "Name: %s \nPrice: %s\nModel: %s\nOriginal: %s\nRebate: %s\nUrlLink: %s\n" %\
                    (thisProduct.name, thisProduct.price['Final'], thisProduct.model,
                     thisProduct.price['Original'], thisProduct.price['Rebate'], thisProduct.imageLink)
                print(displayValues)
                time.sleep(1)
            except Exception as e:
                print(e)
        storageType.closeConnection()

    def print_date_time():
        print
        time.strftime("%A, %d. %B %Y %I:%M:%S %p")

    if __name__ == '__main__':
        schedule.every(.1).minutes.do(retrieveData)
        # schedule.every(1).day.do(retrieveData)
        while 1:
            schedule.run_pending()
            time.sleep(1)