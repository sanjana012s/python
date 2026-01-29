# class include inside data and method and methode is define as, methode are fun that belongs to the ojbject

# class Student():
#   name="sanjna"
# def hello():
#   print("welcome")
# s1=Student()
# print(hello())


class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("welcome", self.name)

s1 = Student("sana")
s1.hello()
