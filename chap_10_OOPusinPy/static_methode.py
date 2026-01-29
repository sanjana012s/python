# static methods: methods that do not use the self parameter(work at class level)
class Student:
  @staticmethod #decorator:changing the behabiour of normal function
  def collage():
    print("ABC collage")
s1=Student()
print(s1.collage())