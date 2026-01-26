#pass fail condition
m1=int(input("enter your marks:"))
m2=int(input("enter your marks:"))
m3=int(input("enter your marks:"))
per=(100*(m1+m2+m3))/300
if(per>=40 and m1>=33 and m2>=33 and m3>=33):
  print("pass",per)
else:
  print("fail with",per,"% because you not pass all sub with 33  marks")