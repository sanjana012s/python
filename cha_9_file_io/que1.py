with open("cha_9_file_io/file.txt","r")as f:
  data=f.read()
  print(data)
  if("sanjana" in data):
    print("name is present in the data")
  else:
    print("name is not present in the data")