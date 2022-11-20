"""
Electronics Showroom:
Laptops, keyboard, bag, mouse, external memory(SSD), headphones

stock of each,
MRP of each,
dealer price,
sell (invoice no), purchase, create order
generate bill
calculate daily/monthly/total profit
"""

from products import Products
from laptop import Laptop
from accessories import Accessories
from headphones import Headphones


"""
l1 = Laptop('hp', 'pavilion', 3, 80000)
h1 = Headphones('boat', 'rockerz', 5, 3000, 1800)
p1 = Products('logitech', 'keyboard', 10, 1500, 900)
p2 = Products('iBall', 'wired mouse', 10, 500, 350)
p3 = Products('iBall', 'wireless mouse', 15, 700, 450)
a1 = Accessories('Sandisk', 'Pen Drive', 20, 1200, 1050, 2)
"""
# print(Products.all_products)
# print(l1)
# Products.printAllStock() 
# print(l1.__class__.__name__)

while True:
    print("Press 1 to make a sell")
    print("Press 2 to make a purchase")
    print("Press 3 to see the inventory")
    print("Press 4 to add new product")
    print("Press 5 to remove an existing product")
    print("Press 6 to edit a product")

    print("Press 8 to exit without saving")
    print("Press 9 to save & exit")

    choice = int(input())

    if choice == 1:
        Products.generateBill()

    elif choice == 2:
        Products.makePurchase()

    elif choice == 3:
        Products.printAllStock()

    elif choice == 4:
        pass

    elif choice == 5:
        pass
    
    elif choice == 6:
        pass
    
    elif choice == 7:
        pass
    
    elif choice == 8:
        break

    elif choice == 9:
        pass