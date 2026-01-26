#print the prime no:

n=int(input("enter the no: "))
sum=0
for i  in range(1,n//2):
  if(n%i==0):
    sum=sum+1
if(sum==2):
  print("no  not  prime: ",n)
else:
  print("no is prime: ",n)
    
 