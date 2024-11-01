# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")
from fontTools.tfmLib import ACCESSABLE

# Create a password checker that:
#
# 	1.	Asks the user to enter a password.
# 	2.	The program will give the user 3 attempts to enter the correct password.
# 	3.	If the password is correct, print "Access Granted!".
# 	4.	If all 3 attempts are incorrect, print "Access Denied!".

correct_password = input("Enter the Secret Password: ")
attempt_count = 0
max_attempts = 3
while attempt_count < max_attempts:
    password = input("Enter the Password: ")
    attempt_count += 1
    if password == correct_password:
        print("Access Granted! ")
        break
    else:
        print("Incorrect password. Try Again! ")
if attempt_count == max_attempts and password != correct_password:
    print("Access Denied! ")