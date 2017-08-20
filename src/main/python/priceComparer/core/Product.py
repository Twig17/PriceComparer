class Product(object):

    def __init__(self, productId, name, price, model):
        self.productId = productId
        self.name = name
        self.model = model
        # price is map with of dates
        # dates have original, rebate, and final prices
        self.price = price


