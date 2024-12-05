g = []

while True:
    try:
        g.append(input().strip())
    except EOFError:
        break

dirs = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
]

n = len(g)
m = len(g[0])

ans = 0
for i in range(n):
    for j in range(m):
        for di, dj in dirs:
            s = ""
            ai, aj = i, j
            it = 0
            while it < 4 and min(ai, aj) >= 0 and ai < n and aj < m:
                it += 1
                s += g[ai][aj]
                ai += di
                aj += dj
            if s in ("XMAS", "SAMX"):
                ans += 1
print(ans)