import csv
from datetime import datetime

class Products():
    ideal_stock = 10
    all_products = []
    all_bills = [] 
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
        with open('products.csv') as f:
            data = csv.DictReader(f)
            for row in data:
                cls(row["brand"], row["category"], int(row["units"]), float(row["mrp"]), float(row["dealer price"]))

    @staticmethod
    def generateBill():
        # date = datetime.today()
        day = input("Enter Bill Date (dd/mm/yyyy): ")
        date = datetime.strptime(day, "%d/%m/%Y")
        current_bill = []
        print("Enter the quantity sold:")
        for product in Products.all_products:
            product.sold = int(input(f'{product.brand} - {product.model}: '))
            billing_price = product.sold * product.mrp
            profit = product.sold * product.profit
            current_bill.append((product.brand, product.model, product.sold, product.mrp, billing_price, profit))
            product.units -= product.sold
        
        print()
        print("Your Bill".center(70, "-"))
        print("Sr.No\t" + "Name\t".expandtabs(30) + "Qty\t" + "Rate\tAmount".expandtabs(10))
        i = 1
        total = 0
        for item in current_bill:
            if item[2] != 0:
                print(f"{i}\t" + f"{item[1]}-{item[0]}\t".expandtabs(30) + f"{item[2]}\t".expandtabs(10) + f"{item[3]}\t{item[4]}".expandtabs(10))
                i += 1
                total += item[4]

        print("-"*70)
        print(f"{total}".rjust(65))
        current_bill.append(date)
        print(current_bill)
        Products.all_bills.append(current_bill)

    @staticmethod
    def makePurchase():
        print("Sr.No\t" + "Name\t".expandtabs(30) + "Price\tStock\tIdeal\tRecomd\tOrder")
        i = 1
        total = 0
        for product in Products.all_products:
            recommended = 0 if product.units >= product.ideal_stock else product.ideal_stock - product.units
            order = int(input(f"{i}\t" + f"{product.brand} - {product.model}\t".expandtabs(30) + f"{product.dealerPrice}\t{product.units}\t{product.ideal_stock}\t{recommended}\t"))
            print("Amount =", product.dealerPrice*order)
            total += product.dealerPrice*order
            
            product.units += order
            i += 1

        print("Total =", total)

    @staticmethod
    def showProfit():
        start = input("From (dd/mm/yyyy): ")
        stop = input("To (dd/mm/yyyy): ")
        begin = datetime.strptime(start, "%d/%m/%Y")
        end = datetime.strptime(stop, "%d/%m/%Y")
        total_profit = 0
        for bill in Products.all_bills:
            if begin <= bill[-1] <=end:
                total_profit += bill[-2]
        print("Total Profit =", total_profit)

if __name__ == "__main__":
    Products.import_from_csv()
    # print(Products.all_products)
    Products.generateBill()
    # Products.makePurchase()