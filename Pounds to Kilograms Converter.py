# Ask the user for their weight in pounds
weight_pounds = float(input("Enter your weight in pounds: "))

# Convert pounds to kilograms (1 pound = 0.453592 kg)
weight_kg = weight_pounds * 0.453592

# Print the result
print(f"Your weight in kilograms is: {weight_kg:.2f} kg")

weight_lbs = input("Weight(lbs): ")
weight_kg = int(weight_lbs)*0.453592
print(weight_kg)
# The line print(f"Your weight in kilograms is: {weight_kg:.2f} kg") is a formatted print statement in Python, and here’s a breakdown of each part:
#
# 	1.	f": The f at the beginning of the string makes it an f-string, which is a special type of string in Python that allows you to include variables directly inside curly braces {} within the string.
# 	2.	"Your weight in kilograms is:: This is plain text that will be printed exactly as written.
# 	3.	{weight_kg:.2f}: This part is an expression inside the f-string. Here’s what each part does:
# 	•	weight_kg: This is a variable that holds the converted weight in kilograms.
# 	•	: .2f: This formatting syntax tells Python to format weight_kg as a floating-point number with 2 decimal places. The f stands for floating point, and .2 specifies that only 2 digits should appear after the decimal point.
# 	4.	kg": This is plain text added after the variable to indicate the units in kilograms.
#
# Full Output Example
#
# If weight_kg is 72.63542, this line will output:
#
# Your weight in kilograms is: 72.64 kg
#
# The value is rounded to two decimal places (72.64) due to the .2f formatting.