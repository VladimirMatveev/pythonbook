a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a,b,c,d)
a[2][1] = 1
print(a,b,c,d)
