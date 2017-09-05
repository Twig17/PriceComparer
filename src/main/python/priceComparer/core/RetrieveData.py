import time
import traceback
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
                displayValues = "Name: %s\nModel:%s\n" %\
                    (thisProduct.name, thisProduct.model)
                print(displayValues)
                time.sleep(1)
            except:
                print(traceback.format_exc())
        storageType.closeConnection()

    def print_date_time():
        print
        time.strftime("%A, %d. %B %Y %I:%M:%S %p")

    if __name__ == '__main__':
        schedule.every(.1).minutes.do(retrieveData)
        while 1:
            schedule.run_pending()
            time.sleep(1)