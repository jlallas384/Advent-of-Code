g = []
while True:
    try:
        g.append(input())
    except EOFError:
        break
n = len(g)
m = len(g[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


vis = [[0] * m for i in range(n)]

def go(i, j):
    vis[i][j] = 1
    q = [(i, j)]
    got = [(i, j)]
    area = 1
    while len(q):
        ci, cj = q.pop()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= min(ni, nj) and ni < n and nj < m and g[ci][cj] == g[ni][nj] and not vis[ni][nj]:
                vis[ni][nj] = 1
                q.append((ni, nj))
                got.append((ni, nj))
                area += 1
    g2 = [[], [], [], []]
    for ci, cj in got:
        for ind, (di, dj) in enumerate(dirs):
            ni, nj = ci + di, cj + dj          
            ok = 0  
            if 0 > min(ni, nj) or ni >= n or nj >= m:
                ok = 1
            elif not (ni, nj) in got:
                ok = 1
            if ok:
                g2[ind].append((ni, nj))
    res = 0
    for xs in g2:
        v2 = [0] * len(xs)
        for i, x in enumerate(xs):
            if v2[i]:
                continue
            q = [x]
            v2[i] = 1
            res += 1
            while len(q):
                ci, cj = q.pop()
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj          
                    if (ni, nj) in xs:
                        ind = xs.index((ni, nj))
                        if not v2[ind]:
                            v2[ind] = 1
                            q.append((ni, nj))     
    return area * res

ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            ans += go(i, j)

print(ans)