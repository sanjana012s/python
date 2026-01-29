# privet(like)attribute and methods:privet attributes and methods are meant to be use only within the class and are not accessible from outside the class

class Account:
  def __init__(self,acc_no,acc_pass):
    self.acc_no=acc_no
    self.__acc_pass=acc_pass#it is public attribute
    #static methods
  def __hello():
    print("sana")
  def reset_pass(self):
    print(self.__acc_pass)
    print(self.__hello())

acc1=Account("12345","abcdef")
print(acc1.acc_no)
# print(acc1.__acc_pass)
print(acc1.reset_pass())
