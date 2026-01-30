# class  method:A class method is bound to the class and receives the class as an implicit first argument

# Note: static method can not access or modifyy class state and generally for utility
class Student:
  @classmethod #decorator
  def college(cls):
    pass