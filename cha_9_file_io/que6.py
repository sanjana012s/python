# que: find out the python present in the file or not


# with open("cha_9_file_io/file6.txt")as f:
#   content=f.read()
# if("python"in content):
#   print("yes python is present")
# else:
#   print("python is not present")


# que: kis line me present hai find karo
with open("cha_9_file_io/file6.txt")as f:
  lines=f.readlines()
lineno=1
for line in lines:
  if("python"in line):
      print("yes python is present  line no:",lineno)
      break
  lineno=lineno+1
else:
  print("python is not present")
    