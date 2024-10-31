x = (10+3) * 2**2
print(x)
# Here are some example problems to help you understand operator precedence in Python. Operator precedence determines the order in which different operations are evaluated in an expression. Python follows a specific order, often remembered by the acronym PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction).
#
# Problem 1: Evaluate Mixed Operations
#
# Consider the following expression:
#
# result = 10 + 2 * 5
# print(result)
#
# Explanation: According to operator precedence, multiplication (*) is evaluated before addition (+). So, 2 * 5 is evaluated first, resulting in 10 + 10, which gives 20.
#
# Expected Output:
#
# 20
#
# Problem 2: Use Parentheses to Change Precedence
#
# Given the following expression, adjust it using parentheses to make addition happen before multiplication.
#
# result = (10 + 2) * 5
# print(result)
#
# Explanation: Adding parentheses around (10 + 2) forces addition to happen first, making it 12 * 5, which results in 60.
#
# Expected Output:
#
# 60
#
# Problem 3: Exponentiation and Multiplication
#
# Evaluate this expression:
#
# result = 2 ** 3 * 4
# print(result)
#
# Explanation: Exponentiation (**) has higher precedence than multiplication (*), so 2 ** 3 is evaluated first, giving 8 * 4, which results in 32.
#
# Expected Output:
#
# 32
#
# Problem 4: Division and Modulus Together
#
# Evaluate this expression and understand the precedence:
#
# result = 10 % 3 + 10 / 2
# print(result)
#
# Explanation: Modulus (%) and division (/) have the same precedence level, so they are evaluated left to right. First, 10 % 3 gives 1, and then 10 / 2 gives 5.0. Finally, 1 + 5.0 results in 6.0.
#
# Expected Output:
#
# 6.0
#
# Problem 5: Combining Multiple Operators with Different Precedences
#
# Evaluate the following expression:
#
# result = 5 + 3 * 2 ** 2 - 8 / 4
# print(result)
#
# Explanation:
#
# 	•	According to precedence rules:
# 	•	** (exponentiation) is evaluated first, so 2 ** 2 becomes 4.
# 	•	Then, * and / are evaluated from left to right, giving 3 * 4 as 12 and 8 / 4 as 2.0.
# 	•	Finally, 5 + 12 - 2.0 is evaluated left to right, resulting in 15.0.
#
# Expected Output:
#
# 15.0
#
# Problem 6: Using Negation with Exponentiation
#
# Evaluate this expression and note the effect of precedence between negation and exponentiation:
#
# result = -3 ** 2
# print(result)
#
# Explanation:
#
# 	•	Exponentiation has higher precedence than negation, so 3 ** 2 is evaluated first, resulting in 9, and then the negation gives -9.
#
# Expected Output:
#
# -9
#
# Tip: To square a negative number, you can use parentheses like this: (-3) ** 2, which would output 9.
#
# Problem 7: Complex Expression with Multiple Operators
#
# Consider the following expression with a combination of operators:
#
# result = (4 + 5) * (3 - 2) ** 2 / 2
# print(result)
#
# Explanation:
#
# 	•	Parentheses are evaluated first: (4 + 5) gives 9 and (3 - 2) gives 1.
# 	•	Then exponentiation is applied: 1 ** 2 gives 1.
# 	•	The expression becomes 9 * 1 / 2, which evaluates as 4.5.
#
# Expected Output:
#
# 4.5
#
# These examples demonstrate Python’s operator precedence rules and show how parentheses can change the order of evaluation. Understanding this order is essential to avoiding unexpected results in complex expressions.