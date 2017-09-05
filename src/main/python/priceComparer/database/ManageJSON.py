import os
import json
import time

from database.ManageStorage import ManageStorage

productInfoFileName = os.path.join(os.path.split(__file__)[0], "../../../resources/productInfoJson.json")
allNeweggProductIdsFilename = os.path.join(os.path.split(__file__)[0], "../../../resources/NeweggProductIds.json")


class ManageJSON(ManageStorage):

    def __init__(self):
        self.website = "Newegg"
        self.file = None
        self.data = {}
        self.currentDate = None

    def setup(self):

        self.currentDate = time.strftime("%d/%m/%Y %H:%M")
        if (os.path.exists(productInfoFileName)) and (os.stat(productInfoFileName).st_size != 0) :
            self.file = open(productInfoFileName, 'r')
            loadedData = self.file.read()
            self.data = json.loads(loadedData)
        else:
            self.file = open(productInfoFileName, 'w')
            self.data = {}

    def closeConnection(self):
        self.file.close

    def writeProduct(self, product):
        # if node exists add the newest price else add new product node to json
        try:
            self.data[product.model]
            self.modifyProduct(product)
        except KeyError as ke:
            self.addProduct(product)

    def addProduct(self, product):
        dataInfo = {}
        dataInfo['name'] = product.name
        dataInfo['productId'] = product.productId
        dataInfo['imageUrl'] = product.imageLink

        priceData = product.detailsList[self.website]
        dateObject = next(iter(priceData))
        dataInfo['prices'] = __createJson(dateObject)
        websiteInfo = {}
        websiteInfo[self.website] = dataInfo
        self.data[product.model] = websiteInfo

        jsonData = json.dumps(self.data)
        with open(productInfoFileName, "w") as file:
            file.write(jsonData)

    def modifyProduct(self, product):
        priceData = product.detailsList[self.website]
        dateObject = next(iter(priceData))
        self.data[product.model][self.website]['prices'][self.currentDate] = self.__createDateJson(dateObject)
        jsonData = json.dumps(self.data)
        with open(productInfoFileName, "w") as self.file:
            self.file.write(jsonData)

    def getAllProductIds(self):
        if (os.path.exists(allNeweggProductIdsFilename)) and (os.stat(allNeweggProductIdsFilename).st_size != 0) :
            productsFile = open(allNeweggProductIdsFilename, 'r')
            allProductIds = productsFile.read()
            productData = json.loads(allProductIds)
            return productData['ids'].keys()
        else:
            return {}

    def __createDateJson(self, dateObject):
        jsonPriceData = {}
        jsonPriceData[dateObject.date] = {}
        jsonPriceData[dateObject.date]['Original'] = dateObject.original
        jsonPriceData[dateObject.date]['Rebate'] = dateObject.rebate
        jsonPriceData[dateObject.date]['Final'] = dateObject.final
        return jsonPriceData
