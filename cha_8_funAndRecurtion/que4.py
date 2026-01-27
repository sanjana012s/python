# sum of  first natural no: using recurtion
def sum():
  n=int(input("enter the no: "))
  if(n==1):
    print(n)
    
  else:
    print(n+sum(n-1))


sum()
    