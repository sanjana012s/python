# que:write a python a program to remane a file to "renamed_by_python.txt
with open("cha_9_file_io/file10old.txt")as f:
  content=f.read()
with open("cha_9_file_io/renamed_by_python.txt","w")as f:
  f.write(content)