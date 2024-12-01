a, b = [], []
for i in range(1000):
    x, y = map(int, input().split("   "))
    a.append(x)
    b.append(y)
a.sort()
b.sort()
print(sum(abs(x - y) for x, y in zip(a, b)))