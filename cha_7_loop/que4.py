
#write a program to find the sum of first n natural no using while loop

# n=int(input("enter the no: "))
# sum=0
# for i in range(1,n+1):
#   sum=sum+i
# print(sum) 

n=int(input("enter the no : "))
i=1
sum=0
while(i<=n):
  sum=sum+i
  i=i+1
print(sum)