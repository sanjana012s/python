# encapsulation:wrapping data and function into a single unit(obj)

# que:creat Account class 2 attr -balance and account no create methode for debit ,credit and printing the balance

class Account:
  def __init__(self,bal,acc):
    self.balance=bal
    self.account_no=acc
  
  #debit methode
  def debit(self,amount):
    self.balance=self.balance-amount
    print("Rs.",amount,"was debited")
    print("total balance=",self.get_balance())
  #credit methode
  def credit(self,amount):
    self.balance=self.balance+amount
    print("Rs.",amount," was credited")
    print("total balance =",self.get_balance())
  def get_balance(self):
    return self.balance

acc1=Account(100,12345)
acc1.debit(100)
acc1.credit(400)
print(acc1.balance)
print(acc1.account_no)