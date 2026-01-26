
# 1 length function
a = "sanjana"
print(len(a))            # 7

# 2 endswith function
print(a.endswith("ana")) # True

# 3 startswith function
print(a.startswith("sanja")) # True

# 4 capitalize function – capitalizes first letter
print(a.capitalize())    # Sanjana

# 5 upper function – converts to uppercase
print(a.upper())         # SANJANA

# 6 lower function – converts to lowercase
print(a.lower())         # sanjana

# 7 title function – first letter of each word
print("hello world".title()) # Hello World

# 8 swapcase function – swaps upper/lower case
print("SaNjA".swapcase()) # sAnJa

# 9 strip function – removes spaces
print("  hi  ".strip())  # hi

# 10 lstrip – removes left spaces
print("  hi".lstrip())   # hi

# 11 rstrip – removes right spaces
print("hi  ".rstrip())   # hi

# 12 replace function
print(a.replace("a", "x")) # sxnjxnx

# 13 find function – first index
print(a.find("a"))       # 1

# 14 rfind function – last index
print(a.rfind("a"))      # 6

# 15 index function
print(a.index("n"))      # 2

# 16 count function
print(a.count("a"))      # 3

# 17 split function
print("a,b,c".split(",")) # ['a','b','c']

# 18 rsplit function
print("a b c".rsplit(" ", 1)) # ['a b','c']

# 19 join function
print("-".join(["a","b","c"])) # a-b-c

# 20 center function
print(a.center(10,"*"))  # *sanjana*

# 21 zfill function
print("99".zfill(5))     # 00099

# 22 isalpha function
print("abc".isalpha())   # True

# 23 isdigit function
print("123".isdigit())  # True

# 24 isalnum function
print("abc123".isalnum()) # True

# 25 isspace function
print("   ".isspace())  # True

# 26 islower function
print(a.islower())      # True

# 27 isupper function
print("ABC".isupper())  # True

# 28 istitle function
print("Hello World".istitle()) # True

# 29 isnumeric function
print("123".isnumeric()) # True

# 30 isdecimal function
print("123".isdecimal()) # True

# 31 casefold function – aggressive lowercase
print("HELLO".casefold()) # hello

# 32 partition function
print("a=b=c".partition("=")) # ('a','=', 'b=c')

# 33 rpartition function
print("a=b=c".rpartition("=")) # ('a=b','=', 'c')

# 34 encode function
print("hi".encode())     # b'hi'

# 35 format function
print("My name is {}".format("Sanjana")) # My name is Sanjana

# 36 format_map function
print("{x}".format_map({"x":10})) # 10

# 37 expandtabs function
print("a\tb".expandtabs(4)) # a   b

# 38 removeprefix function
print("unhappy".removeprefix("un")) # happy

# 39 removesuffix function
print("reading.py".removesuffix(".py")) # reading

# 40 maketrans + translate
table = str.maketrans("a","x")
print(a.translate(table)) # sxnjxnx

# 41 slicing
print(a[1:4])             # anj

# 42 reverse string
print(a[::-1])            # anajnas

# 43 membership operator
print("a" in a)           # True

# 44 not in operator
print("z" not in a)       # True

# 45 concatenation
print(a + " kumari")      # sanjana kumari

# 46 repetition
print(a * 2)              # sanjanasanjana

# 47 len with empty string
print(len(""))            # 0

# 48 bool string
print(bool("hello"))      # True

# 49 bool empty string
print(bool(""))           # False

# 50 ord function
print(ord("A"))           # 65

# 51 chr function
print(chr(65))            # A

# 52 ascii function
print(ascii("π"))         # '\u03c0'

# 53 repr function
print(repr(a))            # 'sanjana'

# 54 f-string
name = "Sanjana"
print(f"My name is {name}") # My name is Sanjana

# 55 enumerate string
print(list(enumerate(a))) # [(0,'s'),...]

# 56 sorted string
print(sorted(a))          # ['a','a','a','j','n','n','s']

# 57 max character
print(max(a))             # s

# 58 min character
print(min(a))             # a

# 59 any function
print(any(a))             # True

# 60 all function
print(all(a))             # True

# 61 string comparison
print("abc" == "abc")     # True

# 62 string comparison
print("abc" > "abb")      # True

# 63 type function
print(type(a))            # <class 'str'>

# 64 id function
print(id(a))              # memory address

# 65 copy string
b = a
print(b)                  # sanjana

# 66 multiline string
print("""Hello
World""")

# 67 escape character
print("Hello\nWorld")

# 68 raw string
print(r"\n")              # \n

# 69 replace space
print("hello world".replace(" ","_")) # hello_world

# 70 count vowels
print(sum(a.count(v) for v in "aeiou")) # 3

# 71 strip characters
print("xxhelloxx".strip("x")) # hello

# 72 ljust
print(a.ljust(10,"*"))    # sanjana***

# 73 rjust
print(a.rjust(10,"*"))    # ***sanjana

# 74 startswith tuple
print(a.startswith(("sa","ka"))) # True

# 75 endswith tuple
print(a.endswith(("na","ra")))   # True

# 76 splitlines
print("a\nb".splitlines()) # ['a','b']

# 77 index error safe
print("a" if "a" in a else "no") # a

# 78 replace once
print(a.replace("a","x",1)) # sxnjana

# 79 center without fill
print(a.center(10))        # ' sanjana '

# 80 string length compare
print(len(a) > 5)          # True

# 81 slicing negative
print(a[-3:])              # ana

# 82 slicing step
print(a[::2])              # s n a a

# 83 remove all spaces
print(" a b c ".replace(" ","")) # abc

# 84 string to list
print(list(a))             # ['s','a','n','j','a','n','a']

# 85 list to string
print("".join(['p','y']))  # py

# 86 upper slice
print(a[:3].upper())       # SAN

# 87 lower slice
print(a[3:].lower())       # jana

# 88 string formatting width
print("{:<10}".format(a))  # sanjana   

# 89 string formatting right
print("{:>10}".format(a))  #    sanjana

# 90 check empty
print(a == "")             # False

# 91 string copy
c = str(a)
print(c)                   # sanjana

# 92 endswith single char
print(a.endswith("a"))     # True

# 93 startswith single char
print(a.startswith("s"))   # True

# 94 title compare
print(a.title())           # Sanjana

# 95 casefold compare
print("ß".casefold())      # ss

# 96 format number
print("{:.2f}".format(3.14159)) # 3.14

# 97 join with space
print(" ".join(a))         # s a n j a n a

# 98 reverse words
print("hello world"[::-1]) # dlrow olleh

# 99 strip newline
print("hi\n".strip())      # hi

# 100 length after strip
print(len(" hi ".strip())) # 2



