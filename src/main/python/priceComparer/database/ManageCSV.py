import abc
import os
import time
from database.ManageStorage import ManageStorage

filename = "../../../resources/productInfo.csv"
file = None


class ManageCSV(ManageStorage):

    def __init__(self):
        self.file = None

    def setup():
        if(self.file is None):
            if os.path.exists(filename):
                self.file = open(filename, 'a')
            else:
                self.file = open(filename, 'w')
                headers = "ProductId,Price,Date,Name\n"
                self.file.write(headers)

    def closeConnection():
        self.file.close

    def writeProduct(product):
        csvValues = "%s,%s,%s,%s,\n" % (
            product.id, product.price.replace(",", ""), time.strftime("%d/%m/%Y"), product.name.replace(",", "|"))
        self.file.write(csvValues)
        print("Wrote to csv file")


