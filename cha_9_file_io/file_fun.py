# f = open("cha_9_file_io/file.txt","r")
# lines=f.readlines()
# print(lines,type(lines))
# f.close()
# it is read the data in list form




#it  is read the only single line
f = open("cha_9_file_io/file.txt","r")
# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# f.close()
line=f.readline()
while(line!=""):
  print(line)
  line=f.readline()
f.close()