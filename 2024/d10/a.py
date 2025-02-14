g = []
while True:
    try:
        s = input()
        g.append(s)
    except EOFError:
        break

n = len(g)
m = len(g[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0

def go(i, j):
    q = []
    q.append((i, j))
    ret = 0
    vis = [[0] * m for i in range(n)]
    vis[i][j] = 1
    while len(q):
        ci, cj = q.pop()
        if g[ci][cj] == '9':
            ret += 1
            continue
        cur = int(g[ci][cj])
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if min(ni, nj) >= 0 and ni < n and nj < m and str(cur + 1) == g[ni][nj] and not vis[ni][nj]:
                vis[ni][nj] = 1
                q.append((ni, nj))
    return ret

for i in range(n):
    for j in range(m):
        if g[i][j] == '0':
            ans += go(i, j)
print(ans)