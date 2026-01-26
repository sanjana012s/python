#items methode give the key value pair

dect={
  "sanjana":200,
  "neha":300,
  "sita":300,
  30000:"root"
}
print(dect.items())


#keys method in that case  it is return the key
print(dect.keys())


#values methode return thr values from dect
print(dect.values())


# upadate methode
dect.update({"sanjana":4,"anu":200})
print(dect)

#get method
print(dect.get("sanjana1"))#return none
print(dect["sanjana1"])#return an error







