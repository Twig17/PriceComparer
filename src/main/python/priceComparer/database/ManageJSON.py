import os
import json
import time

from database.ManageStorage import ManageStorage

filename = os.path.join(os.path.split(__file__)[0], "../../../resources/productInfoJson.json")
productsFilename = os.path.join(os.path.split(__file__)[0], "../../../resources/NeweggProductIds.json")
file = None
data = {}
currentDate = None
website = "Newegg"


class ManageJSON(ManageStorage):
    def setup():
        global file
        global data
        global currentDate

        currentDate = time.strftime("%d/%m/%Y %H:%M")
        if (os.path.exists(filename)) and (os.stat(filename).st_size != 0) :
            file = open(filename, 'r')
            loadedData = file.read()
            data = json.loads(loadedData)
        else:
            file = open(filename, 'w')
            data = {}

    def closeConnection():
        global file
        file.close

    def writeProduct(product):
        global data
        # if node exists add the newest price else add new product node to json
        try:
            data[product.model]
            ManageJSON.modifyProduct(product)
        except KeyError as ke:
            ManageJSON.addProduct(product)

    def addProduct(product):
        global file
        global data
        global currentDate

        dataInfo = {}
        dataInfo['name'] = product.name
        dataInfo['productId'] = product.productId
        dataInfo['imageUrl'] = product.imageLink

        priceData = {}
        priceData[currentDate] = product.price
        dataInfo['prices'] = priceData
        websiteInfo = {}
        websiteInfo[website] = dataInfo
        data[product.model] = websiteInfo

        jsonData = json.dumps(data)
        with open(filename, "w") as file:
            file.write(jsonData)

    def modifyProduct(product):
        global data
        global currentDate

        data[product.model][website]['prices'][currentDate] = product.price
        jsonData = json.dumps(data)
        with open(filename, "w") as file:
            file.write(jsonData)

    def getAllProductIds():
        if (os.path.exists(productsFilename)) and (os.stat(productsFilename).st_size != 0) :
            productsFile = open(productsFilename, 'r')
            allProductIds = productsFile.read()
            productData = json.loads(allProductIds)
            return productData['ids'].keys()
        else:
            return {}
