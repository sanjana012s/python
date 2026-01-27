def fact(n):
  if(n==1 or n==0):
    return 1
  return n*fact(n-1)
n=int(input("enter the no: "))
print("the fact of this no is:",fact(n))