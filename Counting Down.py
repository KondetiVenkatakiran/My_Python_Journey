# Write a program that:
#
# 	1.	Takes an integer n as input from the user.
# 	2.	Uses a while loop to count down from n to 0.
# 	3.	After the loop ends, print "Countdown complete!".
#
# Example: If the user enters 5, the program should print 5, 4, 3, 2, 1, 0 followed by "Countdown complete!".


n = int(input("Enter the number: "))
while n >= 0:
    print(n, end= ' ')
    n -= 1
    print("\n Countdown complete! ")