c1="make a lot of money"
c2="buy now"
c3="subscribe this"
c4="click this"
c=input("enter the comment:")
if((c1 in c)or(c2 in c)or(c3 in c)or(c4 in c)):
  print("this comment is spam")
else:
  print("this comment are not spam")