# if else
# indentation

total_price = 120
discount = 0.9 # 10% off

if total_price >= 100:
    print("You have a discount")
    total_price = total_price * discount
else:
    print("no discount")
    total_price = total_price

print(total_price)
