a, b = [], []
for i in range(1000):
    x, y = map(int, input().split("   "))
    a.append(x)
    b.append(y)
print(sum(x * b.count(x) for x in a))