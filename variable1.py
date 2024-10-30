# name = input('What is your name? ')
# print('Hi '+ name)
name = input('What is your name? ')
color = input('What is your favourite color? ')
print(f"{name} likes {color}")
print(name + ' likes ' + color)
# The line print(f"{name} likes {color}") is a formatted print statement in Python, and here’s a breakdown of each part:
#
# 	1.	f": The f at the beginning of the string makes it an f-string, allowing Python to evaluate expressions inside curly braces {} within the string.
# 	2.	"{name}": This is an expression inside the f-string. The variable name holds the person’s name, and by placing it inside {}, Python will replace {name} with the actual value of the variable.
# 	3.	likes: This is plain text, and it will appear in the output exactly as written.
# 	4.	{color}: Similar to {name}, {color} is also a variable within the f-string. It holds the favorite color of the person, and {color} will be replaced by the actual value of the variable color.
#
# Example
#
# If name = "Mosh" and color = "blue", the line will output:
#
# Mosh likes blue
#
# This use of f-strings allows for clear, readable code when combining variables and text in printed statements.