# f=open("cha_9_file_io/file.txt","r")
# data=f.read()
# print(data)
# f.close()


# if same above code write  with (with fun then we are not close file in this condition)
with open("cha_9_file_io/file.txt","r")as f:
  data=f.read()
  print(data)
    
