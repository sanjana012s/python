word = "Donkey"
with open("cha_9_file_io/file4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("cha_9_file_io/file4.txt", "w") as f:
    f.write(contentNew)
