
a = [0, 4, 2, 3, 1]

for i in a:
    print(i, end=', ')

print()

for i in a:
    print(a[i-1], end='; ')

print()

for i in range(len(a)):
    print(i, end='!')
