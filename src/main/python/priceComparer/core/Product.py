class Product(object):

    def __init__(self, productId, name, price, model, imageLink):
        self.productId = productId
        self.name = name
        self.model = model
        self.imageLink = imageLink
        # price is map with of dates
        # dates have original, rebate, and final prices
        self.price = price


