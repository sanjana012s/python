class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avgs(self):
        res = (self.marks1 + self.marks2 + self.marks3) / 3
        print(self.name, "average marks =", res)

s1 = Student("sanjana", 2, 3, 4)
s1.avgs()
