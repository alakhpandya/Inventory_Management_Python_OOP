from products import Products

class Laptop(Products):
    category = 'Laptop'
    subCategory = 'Regular'
    def __init__(self, brand, model, units, mrp, dealerPrice=0, os='windows'):
        super().__init__(brand, model, units, mrp, dealerPrice)
        self.os = os