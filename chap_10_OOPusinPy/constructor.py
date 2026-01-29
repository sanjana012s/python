class Student:
   def __init__(self):#default constructor
     pass
   collage_name="abc"
   name="anonymous"#class attribute
   def __init__(self,fullname,marks):# parameterized constructor creeeating
    self.name=fullname#self is the referance of object
    self.marks=marks #obj attr>class attr
    print("constructore is calling")

S1= Student("sanjna",89)
print(S1.name)
print(S1.marks)
print(S1.collage_name)




    