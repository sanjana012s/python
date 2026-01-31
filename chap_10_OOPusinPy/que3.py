class Emp:
  def __init__(self,role,dept,salary):
    self.role=role
    self.dept=dept
    self.salary=salary
  def showDetail(self):
    print("role=",self.role)
    print("dept=",self.dept)
    print("salary=",self.salary)
class Engg(Emp):
  def __init(self,name,age):
    self.name=name
    self.age=age
    super().__init("engg","it","10000000")

# e1=Emp("accountant","finance","60,000")
# e1.showDetail()


e1=Engg("elin musk","60,000","678")
e1.showDetail()