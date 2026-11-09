#Declare and initialize variables
nameItem = "TV Stand"
retailPrice = 0.00
wholesalePrice = 0.00
profit = 0.00
salePrice = 0.00
saleProfit = 0.00
SALE_PRICE_RATE = 0.25

#Prompt for input and assign to the proper variables
nameItem = str(input("Please enter the name of the item: "))
retailPrice = float(input("Please enter the retail price of the intem: "))
wholesalePrice = float(input("Please enter the wholesale price of the item: "))

#Calculate sale price and sale profit
profit = round(retailPrice - wholesalePrice,2)
salePrice = round(retailPrice * (1 - SALE_PRICE_RATE),2)
saleProfit = round(salePrice - wholesalePrice,2)

#Display the results
print(f"Item Name:{nameItem}")
print(f"Retail Price: ${retailPrice:.2f}")
print(f"Wholesale Price: ${wholesalePrice:.2f}")
print(f"Profit: ${profit:.2f}")
print(f"Sale Price: ${salePrice:.2f}")
print(f"Sale Profit: ${saleProfit:.2f}")