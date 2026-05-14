# s="Logicwhile"
# print(s.isalpha())

# s="12345"
# print(s.isdigit())

# s="sravs73"
# print(s.isalnum())

# s="sravss"
# print(s.islower())
# print(s.isupper())

# s="R Sravanthi"
# print(s.startswith("R"))
# print(s.endswith("sravanthi"))


# while True:
#    s=input()
#    if s.isalpha():
#      print("alphabets")
#    elif s.isdigit():
#     print("digit number")
#    elif s.isalnum():
#       print("number and names")
#    elif s.islower():
#       print("lower case")
#    elif s.isupper():
#       print("upper case")


# s="sravs is suji friend"
# print(s.find("friend"))

# s="suji sravs praggu they three are friends"
# print(s.replace("s","p"))

# s="      This is sravanthi   "
# print(s)
# print(s.strip())
# print(s.rstrip())

# s="This is sravanthi"
# print(s.split())
# print(s.partition("This"))

# s="logicwhile"
# psrint("^".join(s))

# s="Sravanthi"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# for i in range(1,129):
#     print(i,chr(i),end="")


# name = "Sravanthi"
# for ch in name:
#     print(ch, "=", ord(ch))

# for i in "sravanthi":
#     print(i,"=",ord(i))

# s="sravanthi"
# print(s[::-1])

# s="sravanthi"
# rev=""
# for i in "sravanthi":
#     rev=i+rev
# print(rev)

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")


