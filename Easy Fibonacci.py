n = int(input())

a, b = 0, 1

for i in range(n):
    if i == n - 1:
        print(a)
    else:
        print(a, end=' ')
    a, b = b, a + b