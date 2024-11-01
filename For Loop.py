# for item in ['kiran','tarun','varun','karan']:
#     print(item)
# for item in range(10 ,20, 3):
#     print(item)
# for item in [1,2,3,4,5,6,7,8,9]:
#     print(item)
from numpy.testing.print_coercion_tables import print_new_cast_table

prices = [10,20,30]
total = 0
for price in prices:
    total +=price
print(f"Total: {total}")

# Write a program that calculates the sum of all integers from 1 to 100.
total_sum = 0
for number in range(1, 101):
    total_sum += number
print("The sum of number from 1 to 100 is: ", total_sum)

# Write a program that prints the multiplication table for a given number (e.g., 5) from 1 to 10.
n = int(input("Enter the number: "))
i=1
for i in range(1,10):
    result = n*i
    print(f"{n} X {i} = {result}")
# Write a program that calculates the factorial of a given number (e.g., 5).

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
number = int(input("Enter the number: "))

fact = factorial(number)

print(f"The factorial of {number} is: {fact}")



#Write a program that generates a list of squares of numbers from 1 to 20.

for n in range(1,21):
    n = n**2
    print(n)
