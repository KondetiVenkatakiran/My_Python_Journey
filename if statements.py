from logging import fatal
from turtledemo.forest import doit1

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("it's a lovely day")
print("Enjoy your day")


price = float(input("Enter the price of house: "))
has_good_credit = False
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down Payment: ${down_payment}")



