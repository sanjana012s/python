class Car:
  @staticmethod
  def start():
    print("car is started")
  
  @staticmethod
  def stop():
    print("car is stop")
    
class ToyotaCar(Car):
  def __init__(self,brand):
    self.brand=brand


class Fortuner(ToyotaCar):
  def __init__(self,type):
    self.type=type


car1=Fortuner("diesel")
print(car1.start())
    