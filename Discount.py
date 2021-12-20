price1 = float(input("enter the price of first drink: "))
price2 = float(input("enter the price of second drink: "))
if price1 < price2:
    discountvalue = price1 /2
else:
    discountvalue= price2 /2
totalprice = price1 + price2 - discountvalue
print ("total price is:" ,totalprice)
