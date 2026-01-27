f=open("cha_9_file_io/file.txt","a")
f.write("sanjana is smart girl")
f.close()



f = open("cha_9_file_io/file.txt", "r+")
print(f.read())
f.write("\nNew line added")
f.close()


f = open("cha_9_file_io/file.txt", "w+")
f.write("Hello Python")
f.seek(0)
print(f.read())
f.close()


f = open("cha_9_file_io/file.txt", "a+")
f.write("\nThis is appended text")
f.seek(0)
print(f.read())
f.close()

# Mode     	Kaam
# r+	      Read + Write (no delete)
# w+	      Write + Read (delete old data)
# a+       	Append + Read