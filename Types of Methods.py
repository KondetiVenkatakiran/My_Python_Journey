
class Student:
    school = "Kent State University"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #     instance method
    # these are two types
    # Accessor Methods - for fetch the value
    # mutator Methods - for mutate the value
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # these are Accessors
    def get_m1(self):
        return self.m1
    #  these are mutators
    def set_m1(self,value):
        self.m1 = value
    @classmethod
    def info(cls):
        return cls.school
s1 = Student(34,67,89)
s2 = Student(23,45,67)

print(f"{s1.avg()} {s2.avg()}")
print(Student.info())