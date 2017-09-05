class Product(object):

    def __init__(self, productId, name, price, model, imageLink, detailsList):
        self.productId = productId
        self.name = name
        self.model = model
        self.imageLink = imageLink
        # price is map of Dates
        # Dates have original, rebate, and final prices
        self.price = price
        self.detailsList = detailsList


