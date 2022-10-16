

# a = 5.5
# print(isinstance(a, int))
# print(isinstance(a, float))
# b = 7.0
# print(isinstance(b, int))
# print(isinstance(b, float))
# print(a.is_integer())
# print(b.is_integer())

# a = float(input("Enter any number: "))
# if a.is_integer():
#     a = int(a)
# print("a =", a)


# without using csv module

# f = open('temp.csv')
# data = f.readlines()
# # print(data)
# for line in data:
#     row = line.split(",")
#     print(row)
# f.close()

import csv

# f = open('temp.csv')
# data = csv.reader(f)
# # print(data)
# header = next(data)
# for row in data:
#     print(row)

# print(header)
# f.close

with open('products.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in list(data):
        print(row)
        print()