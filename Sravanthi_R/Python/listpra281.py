# lst = [1, 2, 2, 3, 4, 3, 5]
# n= []
# for i in lst:
#     if i not in n:
#         n.append(i)
# print(n)


# lst = [10, 5, 20, 8, 15]
# lrg= lst[0]
# sec= lst[0]
# for i in lst:
#     if i > lrg:
#         sec = lrg
#         lrg = i
#     elif i > sec and i != lrg:
#         second = i
# print("Sec lrg:", sec)


# lst = [1, 2, 3, 4, 5]
# k = 2
# k = k % len(lst)
# rotated = lst[-k:] + lst[:-k]
# print(rotated)


# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# common = []
# for i in lst1:
#     if i in lst2 and i not in common:
#         common.append(i)
# print(common)


# lst = [1, 2, 3, 4, 5, 6]
# evn = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         evn.append(i)
#     else:
#         odd.append(i)
# print("Evn:", evn)
# print("Odd:", odd)