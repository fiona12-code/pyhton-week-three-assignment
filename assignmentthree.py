def calculate_discount(price, discount_percent):
    price = float(price)
    discount_percent = float(discount_percent)
    calculate_discount = price * discount_percent
    return calculate_discount

#-- Test Cases --#
price = float(120.00)
discount_percent = float(0.20)
calculate_discount = price * discount_percent
if discount_percent >= 0.20:
    print(f"You get a discount of 20%")
else:
    print(price)

    #-- prompt user for price and discount percent --#
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))
calculate_discount = price * discount_percent

#-- print --#
if discount_percent >= 0.20:
    print(f"You get a discount of 20%")
else:
    print(price)
    