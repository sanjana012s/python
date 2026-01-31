# polymorphism:operator overloading
# when the same operator is allowed to have different meaning according to the context


# operator and dunder fnction
# a+b  add     a__add__(b)


class Complex:
  def __init__(self,real,img):
    self.real=real
    self.img=img
  def showNo(self):
    print(self.real,"i +",self.img,"j")
  def __add__(self,num2):
    newReal=self.real+num2.real
    newImg=self.img+num2.img
    return Complex( newReal,newImg)
    

num1=Complex(1,3)
num1.showNo()
num2=Complex(1,3)
num2.showNo()
num3=num1+num2
num3.showNo()

# num3=num1.add(num2)
# num3.showNo()
