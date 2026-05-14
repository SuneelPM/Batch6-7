# n=3
# for i in range(1,10+1):
#  print(n,"*",i,"=",n*i)

# n=3
# for i in range(1,10+1):
#     print("%d*%2d=%2d"%(n,i,n*i))

# for i in range(2):
#     for j in range(2):
#         print(i,j)

# for i in range(2, 10+1):
#     for j in range(1, 10+1):
#         print(i, "x", j, "=", i*j)
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# n = 5
# for rows in range(1, n+1):
#     for spaces in range(1, n-rows+1):
#         print(" ", end=" ")
#     for cols in range(1, 2*rows):
#         print("*", end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#      print("*",end="")
#     print()

n=int(input())
for i in range(1,n+1):
    print("*" *n)
print()

