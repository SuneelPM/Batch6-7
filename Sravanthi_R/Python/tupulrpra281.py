# tpl = (1, 2, 3, 2, 4, 2)
# key = 2
# count = 0
# for i in tpl:
#     if i == key:
#         count += 1
# print(count)


# tpl = (10, 5, 20, 3, 15)
# lrg= tpl[0]
# sml = tpl[0]
# for i in tpl:
#     if i > lrg:
#         lrg = i
#     if i < sml:
#         sml= i
# print(lrg)
# print(sml)


# tpl = (1, 2, 3, 4, 2)
# r= 2
# n= tuple(i for i in tpl if i != r)
# print(n)


# tpl = (5, 1, 4, 2, 3)
# lst = list(tpl)
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# st= tuple(lst)
# print(st)


# tpl = (1, 2, 3, 4, 5, 6)
# k = 7
# for i in range(len(tpl)):
#     for j in range(i + 1, len(tpl)):
#         if tpl[i] + tpl[j] == k:
#             print((tpl[i], tpl[j]))