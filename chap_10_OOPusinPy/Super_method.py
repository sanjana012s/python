# super method:super()method is used to access methods of the parent class
class Car:
  def __init__(self,type):
    self.type=type
  
  @staticmethod
  def start():
    print("car is start..")
  @staticmethod
  def stop():
    print("car is stop")
  class ToyotaCar(Car):
    def __init__(self,name,type):
       super().__init__(type)

       self.name=name
       super().start()



car1=ToyotaCar("prius","electric")
print(car1.type)