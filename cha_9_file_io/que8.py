with open("cha_9_file_io/file7.txt")as f:
  content1=f.read()
with open("cha_9_file_io/file7_copy.txt")as f:
  content2=f.read()
if(content1==content2):
  print("file is identical")
else:
  print("file is not identical")