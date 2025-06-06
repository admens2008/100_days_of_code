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

# # built-in funtctions

# a = [1, 2, 3, 4, 5]

# print(a.index(4))
# a.reverse()
# print(a)
# a.insert(1, 69)
# print(a)
# a.clear()
# print(a)

# b = [2, 34]
# c = a + b
# print(c)

# # fibonacci sequence

# num = [0, 1]

# for i in range(98):
#     sum = num[-1] + num[-2]
#     num.append(sum)
# print(num)

# # building new lists, repeating and empty
# x = [2, 4, 7, 8]
# y = x * 3
# print(y)

# # List comprehension
# a = [1, 2, 3, 4, 5, 6]

# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i * 4)
# print(b)

# using list comprehension to solve same problem
a = [1, 2, 3, 4, 5, 6]
b = [i * 4 for i in a if i % 2 == 0]
print(b)