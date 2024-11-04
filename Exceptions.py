

try:
    age = int(input("age: "))
    income = int(input("Enter the income: "))
    risk = income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print('Invalid value')
