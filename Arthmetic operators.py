# from typing import final
#
# from IPython.lib.pretty import pprint
# from scipy.constants import minute
#
# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3)
# print(10**3)
# print(10%3)
# # Given the length and width of a rectangle, find its area using the multiplication operator *.
# length = int(input("Enter the Length:"))
# width = int(input("Enter the width: "))
# area = length*width
# print("Area of the rectangle:",area)
#
# # Given a total number of minutes, use floor division // and modulus % to convert it to hours and remaining minutes
# total_minutes = float(input("Enter the no of min: "))
# hours = total_minutes//60
# minutes = total_minutes % 60
# print(type(total_minutes))
# print(type(hours))
# print(type(minutes))
# print(f"{total_minutes} minutes is equals to {hours} hour(s) and {minutes} minute(s)")
# print(total_minutes ," minutes is equal to ", hours , " hours and " ,minutes, " minutes")
#
# # If a product’s price is $120 and the tax rate is 8%, calculate the final price by using multiplication and addition.
# price = float(input("Enter the price: "))
# tax_rate = float(input("Enter the tax: "))
# tax = price * tax_rate
# final_price = price + tax
# print("final price: ",final_price)
#
# # 5. Compound Interest Calculation
# #
# # Given a principal amount, rate, and time, calculate the amount after interest using exponentiation **.
# #
# #
# # \text{Amount} = \text{Principal} \times (1 + \frac{\text{Rate}}{100})^{\text{Time}}
#
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate: "))
# time =float(input("Enter the time:"))
# amount = principal* (1+rate/100)**time
# print("Final amount: ",amount)


x = 10
x = x+3
print(x)
y = 10
y += 3
print(y)
z = 90
z -= 60
print(z)


# Create a calculator that performs basic arithmetic operations.
#  here I amd defining function for every operation
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "Error! Division by Zero."
    return x/y

# Display option for the user
print("Select operation: ")
print("1. Add +")
print("2. Sub -")
print("3. Mul *")
print("4. Div / ")

# Take input from the user
user_choice = input("Enter choice (1/2/3/4): ")
if user_choice in ['1' ,'2' ,'3' ,'4']:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if user_choice == '1':
            print(f"The result: {add(num1,num2)}")
        elif user_choice == '2':(
            print(f"The result: {sub(num1,num2)}"))
        elif user_choice == '3':(
            print(f"The result: {mul(num1,num2)}"))
        elif user_choice == '4':(
            print(f"The result: {div(num1,num2)}"))
    except ValueError:
        print("Invalid input! Please enter a valid number. ")

else:
    print("Invalid input! Please enter the valid operator")
