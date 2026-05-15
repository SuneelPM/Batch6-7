# s=input()
# fchr=s[0]
# rslt=fchr
# for ch in s[1:]:
#     if ch==fchr:
#         rslt+="$"
#     else:
#         rslt+=ch
# print(rslt)


# s=input()
# fc=s[0]
# for i in range(len(s)):
#     if s[i]==fc.lower() or s[i]==fc.upper():
#         s=s[:i]+"$"+s[i+1:]
#     res=fc+s[1:]
# print(res)

# s=input()
# if len(s)>=3:
#     if s.endswith("ing"):
#       ns=s+"ly"
#     else:
#         ns=s+"ing"
# else:
#     ns=s
# print(ns)


# s=input()
# a=s.split()
# m=0
# for i in a:
#     if len(i)>m:
#         m=len(i)
# print(m)

# list=[73,786,'S','S',"ss",73.3,True,False]
# print(list)
# print(type(list))

# list=[11,22,33,[44,55,66],77,88]
# print(list[0])

# s="firoze"
# vowels="aeiou"
# v=0
# c=0
# for i in s:
#     if i in vowels:
#         v+=1
#     else:
#         c+=1
# print(v)
# print(c)

# s="access"
# cnt=0
# for i in s:
#     cnt+=1
# print(cnt)

# s = "Sravanthi@73"
# count= 0
# for ch in s:
#     if ch.isupper():
#         count+= 1
# print(count)


# s = "Sujitha@143"
# count = 0
# for ch in s:
#     if ch.islower():
#         count += 1
# print(count)


# s = "Pragna@699"
# result = ""
# for ch in s:
#     if ch.isupper():
#         result += ch.lower()
#     elif ch.islower():
#         result += ch.upper()
#     else:
#         result += ch 
# print(result)


# s = "Sravanthi"
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)


# s = "banana"
# for ch in set(s):
#     print(ch, ":", s.count(ch))


# s = "banana"
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)


# s = "Python is very easy"
# length = 0
# for ch in s[::-1]:
#     if ch == " ":
#         break
#     length += 1
# print(length)


# s = "programming"
# seen = ""
# for ch in s:
#     if ch in seen:
#         print(ch)
#         break
#     else:
#         seen += ch


# s = "programming"
# for ch in s:
#     count = 0
#     for c in s:
#         if ch == c:
#             count += 1
#     if count == 1:
#         print( ch)
#         break


# s = "programming"
# ch = "g"
# first = -1
# last = -1
# for i in range(len(s)):
#     if s[i] == ch:
#         if first == -1:
#             first = i
#         last = i
# if first == -1:
#     print("Character not found")
# else:
#     print( first)
#     print( last)