N = int(input())

for i in range (N) :
    a, b, c = map(float, input().split())
    average = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f"{average:.1f}")