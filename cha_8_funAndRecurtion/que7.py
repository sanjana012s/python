# remove word from list
def rem(list,word):
  for i in list:
    list.remove(word)
    return list
list=["sanjana","neha"]
print(rem(list,"neha"))




def strip(l,word):
  n=[]
  for item in l:
    if not(item==word):
      n.append(item.strip(word))
  return n
l=["sanjana","neha","gita","ta"]
print(strip(l,"ta"))