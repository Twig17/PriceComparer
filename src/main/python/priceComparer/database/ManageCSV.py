import abc
import os
import time
from database.ManageStorage import ManageStorage

filename = "../../../resources/productInfo.csv"
file = None


class ManageCSV(ManageStorage):

    def setup():
        global file
        if(file is None):
            if os.path.exists(filename):
                file = open(filename, 'a')
            else:
                file = open(filename, 'w')
                headers = "ProductId,Price,Date,Name\n"
                file.write(headers)

    def closeConnection():
        global file
        file.close

    def writeProduct(product):
        global file
        csvValues = "%s,%s,%s,%s,\n" % (
            product.id, product.price.replace(",", ""), time.strftime("%d/%m/%Y"), product.name.replace(",", "|"))
        file.write(csvValues)
        print("Wrote to csv file")


