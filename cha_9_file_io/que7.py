with open("cha_9_file_io/file7.txt")as f:
  content=f.read()
with open("cha_9_file_io/file7_copy.txt","w")as f:
  f.write(content)