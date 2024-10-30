
first = 'kiran'
last = 'kondeti'
message = first+ ' [' +last+ '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)


# The line msg = f'{first} [{last}] is a coder' is a Python statement that creates a formatted string and assigns it to the variable msg. Here’s a detailed breakdown of each part:
#
# 	1.	msg =: This part of the statement assigns the resulting string to the variable msg. This variable can then be used later in the code to reference this string.
# 	2.	f'...': The f before the string indicates that it is an f-string (formatted string literal). This allows for embedding expressions inside curly braces {} within the string, enabling the insertion of variable values directly into the string.
# 	3.	{first}: Inside the f-string, {first} is a placeholder for the variable first. When the string is evaluated, Python replaces {first} with the actual value of the variable first. This variable is expected to contain a string (likely representing a first name).
# 	4.	[{last}]: Similarly, {last} is another placeholder for the variable last. The square brackets around {last} format the output so that the last name appears within brackets in the final string. When evaluated, this part will be replaced with the value of last, which is also expected to be a string (likely representing a last name).
# 	5.	is a coder: This is plain text that will be included in the resulting string exactly as written.
#
# Example
#
# If first = "Kiran" and last = "Kondeti", the line will produce the following string:
#
# msg = 'Kiran [Kondeti] is a coder'
#
# Summary
#
# 	•	The line creates a formatted string that incorporates the values of the first and last variables, resulting in a sentence that states who the person is. This string is stored in the variable msg, which can then be printed or used later in the program.