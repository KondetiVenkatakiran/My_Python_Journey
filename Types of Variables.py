class Car:
    # these are class(static) variables
    wheels = 4
    def __init__(self):
        # These are Instance variables
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

Car.wheels = 5

print(f"{c1.com} {c1.mil} {c1.wheels}")
print(f"{c2.com} {c2.mil} {c2.wheels}")