# # lists
# x = [10, 4, 1, 98]

# y = x[0]
# z = x[-1]
# print(y, z)

# a = x[1 : -1]
# print(a)

# x[1] = 12 
# # lists are mutable. u can cahnge ind elements inside a list without creating a new list
# print(x)

# 3 ways to force a copy
# c = x.copy()
# d = x[:]
# e = list(x)
# print(c)
# print(d)
# print(e)

# # for lists

# x = [23, 1, 45, 32, 30, 21, 64]

# for i in x:
#     print(i, end=" ")
# print()


# a = [6, 2, 1, 32, 67]

# for i in range(len(a)):
#     print(a[i], end=" ")
# print()

# for and enumerate()
# getting both the elements and the indexes

# b = [6, 2, 1, 32, 67]

# for i, j in enumerate(b):
#     print(i, j)

# # doubling the values
# # prg that goes thru a list, if an element is even, mulitply by 2. do nothing if its odd

# i = [6, 2, 1, 32, 67]
# x = [1, 2, 3, 4, 5, 6]

# for x in i:
#     if x % 2 == 0:
#         x *= 2
#     print(x)

# for i, j in enumerate(x):
#     if j % 2 == 0:
#         x[i] = j * 2
# print(x)
