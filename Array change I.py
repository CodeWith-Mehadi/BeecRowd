N = []

for _ in range(20):
    num = int(input())
    N.append(num)

for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]

for i in range(20):
    print(f"N[{i}] = {N[i]}")
