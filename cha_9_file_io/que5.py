words=["Donkey","bad"]
with open("cha_9_file_io/file5.txt","r")as f:
  content=f.read()
for word in words:
  content=content.replace(word,"#"*len(word))
with open("cha_9_file_io/file5.txt","w")as f:
  f.write(content)