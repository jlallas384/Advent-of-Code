g = []

while True:
    try:
        g.append(input().strip())
    except EOFError:
        break

dirs = [
    ((-1, -1), (1, 1)),
    ((-1, 1), (1, -1)),
]

dirs = dirs + [(y, x) for x, y in dirs ]
n = len(g)
m = len(g[0])

ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if g[i][j] != 'A':
            continue
        cnt = 0
        for (y1, x1), (y2, x2) in dirs:
            if g[i + y1][j + x1] == 'S' and g[i + y2][j + x2] == 'M':
                cnt += 1
        if cnt == 2:
            ans += 1
print(ans)