#Discount Calculation
#Write a python program to calculate the price of an item after a discount.
# Calculate the price of an item that costs $ 200 after a 15% discount
print ("DISCOUNT PRICE CALCULATOR")
original_price = float(input('Original Price: '))
Discount = float(input("Enter Discount percentage: "))
k = (Discount * original_price) / 100
t = original_price - k
discounted_price = t
print("discounted price is " + str(k))
print("Amount payable after discount = " + str(discounted_price))