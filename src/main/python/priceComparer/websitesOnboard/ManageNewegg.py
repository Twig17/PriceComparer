from websitesOnboard.ManageWebsites import ManageWebsites
import core.Dates as Dates
import core.ProductDetails as ProductDetails
import core.Product as Product
import json
import time
import requests


class ManageNewegg(ManageWebsites):

    def __init__(self):
        self.websiteName = 'Newegg'

    def getDataProduct(self, productId):
        currentDate = time.strftime("%d/%m/%Y %H:%M")
        websiteUrl = requests.get("http://www.ows.newegg.com/Products.egg/%s" % productId)
        pageJson = websiteUrl.json()

        # {} is for default value instead of null
        nameDesc = pageJson.get("Basic", {}).get("Title")
        price = pageJson.get("Basic", {}).get("FinalPrice")
        model = pageJson.get("Additional", {}).get("Model")
        originalPrice = pageJson.get("Basic", {}).get("OriginalPrice")
        rebate = pageJson.get("Basic", {}).get("RebateText")
        imageUrl = pageJson.get("Basic", {}).get("ItemImages", {})[0].get("PathSize640", {})

        product = Product
        product.model = model
        productDetails = ProductDetails
        productDetails.name = nameDesc
        productDetails.imageLink = imageUrl
        productDetails.productId = productId
        productDetails.price = {}
        datePriceInfo = Dates
        datePriceInfo.date = currentDate
        datePriceInfo.original = originalPrice
        datePriceInfo.rebate = rebate
        datePriceInfo.final = price
        productDetails.price[currentDate] = datePriceInfo
        product.detailsList = {}
        product.detailsList[self.websiteName] = productDetails

        return product
