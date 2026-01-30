# Inheritance:when one class (child/derived)derives the properties and methods of another class(parent/base).

class Car:
  @staticmethod
  def start():
    print("car is started..")
  
  @staticmethod
  def stop():
    print("car stopped.")
    
#derive class
class ToyotaCar(Car):
  def __init__(self,name):
    self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.name)
print(car1.stop())