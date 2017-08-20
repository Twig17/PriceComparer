from websitesOnboard.ManageWebsites import ManageWebsites
import json
import requests

class ManageNewegg(ManageWebsites):

    def getDataProduct(product):
        websiteUrl = requests.get("http://www.ows.newegg.com/Products.egg/%s" % product.productId)
        pageJson = websiteUrl.json()

        # {} is for default value instead of null
        nameDesc = pageJson.get("Basic", {}).get("Title")
        price = pageJson.get("Basic", {}).get("FinalPrice")
        model = pageJson.get("Additional", {}).get("Model")
        originalPrice = pageJson.get("Basic", {}).get("OriginalPrice")
        rebate = pageJson.get("Basic", {}).get("RebateText")
        imageUrl = pageJson.get("Basic", {}).get("ItemImages", {})[0].get("PathSize640", {})

        product.name = nameDesc
        product.model = model
        product.imageLink = imageUrl
        allPrices = {}
        allPrices['Original'] = originalPrice
        allPrices['Rebate'] = rebate
        allPrices['Final'] = price
        product.price = allPrices
        return product
