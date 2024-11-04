

class Computer:
    def __init__(self):
        self.name = "Kiran"
        self.age = 22
    def update(self):
        self.age = 21
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()
c1.update()
if c1.compare(c2):
    print("They are same... ")
else:
    print("They are different....")



print(f"{c1.name} {c1.age}")
print(f"{c2.name} {c2.age}")
print(id(c1))
print(id(c2))