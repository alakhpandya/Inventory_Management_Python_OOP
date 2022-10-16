from products import Products

class Accessories(Products):
    category = 'Accessories'
    def __init__(self, brand, model, units, mrp, dealerPrice=0, broken=0):
        super().__init__(brand, model, units, mrp, dealerPrice)
        self.broken = broken