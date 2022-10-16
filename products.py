
class Products():

    all_products = []
    def __init__(self, brand, model, units, mrp, dealerPrice = 0):
        assert brand.__class__.__name__ == 'str', f'Please enter string only'
        assert model.__class__.__name__ == 'str', f'Please enter string only'
        assert units.__class__.__name__ == 'int', f'Please enter integers only'
        assert units >= 1, f'Value {units} is invalid for units, please enter positive integers only...'
        '''
        try:
            assert units >= 1
        except AssertionError:
            print(f'Value {units} is invalid for units, please enter positive integers only...')
        '''
        # if mrp.__class__.__name__ == 'float':
        if isinstance(mrp, float):
            pass
        elif mrp.__class__.__name__ == 'int':
            pass
        else:
            raise Exception ('Please enter numbers only')
        
        assert mrp > 0, f'Value {mrp} is invalid for units, please enter positive number only...'


        self.brand = brand
        self.model = model
        self.units = units
        self.mrp = mrp
        self.dealerPrice = dealerPrice

        Products.all_products.append(self)

        self.profit = self.mrp - self.dealerPrice


    def calculateProfit(self, soldUnits):
        return self.profit * soldUnits

    def __repr__(self) -> str:      # repr: representation
        return f'{self.__class__.__name__}("{self.brand}", "{self.model}", "{self.units}", "{self.mrp}", "{self.dealerPrice}", "{self.profit}")'

    @staticmethod
    def printAllStock():
        print('Sr.No.\t' + 'Category\tSub Category\tBrand\tModel\t'.expandtabs(15) + 'Stock\tMRP\t'.expandtabs(8) + 'Dealer Price\tProfit'.expandtabs(15))
        sr = 1
        for product in Products.all_products:
            print(f'{sr}\t' + f'{product.category}\t{product.subCategory}\t{product.brand}\t{product.model}\t'.expandtabs(15) + f'{product.units}\t{product.mrp}\t'.expandtabs(8) + f'{product.dealerPrice}\t{product.profit}'.expandtabs(15))
            sr += 1

    @classmethod
    def import_from_csv(cls):
        pass