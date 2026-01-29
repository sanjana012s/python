#abstractions: hiding the implementation details of a class and only showing the important features to the user

class Car:
  def __init__(self):
    self.acc=False
    self.brk=False
    self.clutch=False
  def start(self):
    self.clutch=True
    print("car is started..")

car1=Car()
car1.start()