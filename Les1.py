a = {i * 1 for i in range(5)}
b = {i * 2 for i in range(5)}
c = {i * 4 for i in range(5)}

###объединение
x1 = set.union(a, b, c)
x_1 = a | b | c

###пересечение
x2 = set.intersection(a, b, c)
x_2 = a & b & c

###симметрическая разность множеств
x3 = a ^ b ^ c

###разность множеств
x4 = (a - b, a - c, b - a, b - c, c - a, c - b)




print(a, b, c)
print(x1)
print(x2)
print(x3)
print(x4)
print(x_1)
print(x_2)