# Write a program that:
#
# 	1.	Takes an integer n from the user.
# 	2.	Uses a while loop to print the multiplication table for n (up to n * 10).
#
# Example: If the user enters 3, the program should print 3 x 1 = 3, 3 x 2 = 6, … up to 3 x 10 = 30.
from numpy.core.multiarray import result_type

n = int(input("Enter the number: "))
i = 1
while i <= 10:
    result = n*i
    i += 1
    print(f"{n} X {i} = {result}")