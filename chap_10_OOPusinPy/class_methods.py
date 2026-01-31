# class  method:A class method is bound to the class and receives the class as an implicit first argument

# Note: static method can not access or modifyy class state and generally for utility




# class Student:
#   @classmethod #decorator
#   def college(cls):
#     pass


# class Person:
#   name="anonymous"
#   def changeName(self,name):
#     self.__class__.name="sana"


# p1=Person()
# p1.changeName("sana khatoon")
# print(p1.name)
# print(Person.name)



class Person:
  name="anonymous"
  @classmethod #decorator
  def changeName(cls,name):
    cls.name=name


p1=Person()
p1.changeName("sana khatoon")
print(p1.name)
print(Person.name)
