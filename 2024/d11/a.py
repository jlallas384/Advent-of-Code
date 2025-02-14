a = list(map(int, input().split()))

for i in range(25):
    b = []
    for x in a:
        if x == 0:
            b.append(1)
        elif len(str(x)) % 2 == 0:
            g = str(x)
            b.append(int(g[:len(g) // 2]))
            b.append(int(g[len(g) // 2:]))
        else:
            b.append(x * 2024)
    a = b
print(len(a))