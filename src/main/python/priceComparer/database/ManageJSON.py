import os
import json
import time

from database.ManageStorage import ManageStorage

filename = "../../../resources/productInfoJson.txt"
file = None
data = {}


class ManageJSON(ManageStorage):
    def setup():
        global file
        global data
        if (file is None):
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
            data[product.id]
            ManageJSON.modifyProduct(product)
        except KeyError as ke:
            ManageJSON.addProduct(product)

    def addProduct(product):
        global file
        global data

        dataInfo = {}
        dataInfo['name'] = 'product name'  # product.name

        priceData = {}
        priceData[time.strftime("%d/%m/%Y")] = product.price
        dataInfo['prices'] = priceData
        data[product.id] = dataInfo

        jsonData = json.dumps(data)
        with open(filename, "w") as file:
            file.write(jsonData)

    def modifyProduct(product):
        global data
        data[product.id]['prices']['20/08/2017'] = '$17'
        # loadedData[product.id]['prices'][time.strftime("%d/%m/%Y")] = product.price
        jsonData = json.dumps(data)
        with open(filename, "w") as file:
            file.write(jsonData)
