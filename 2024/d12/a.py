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
    outer = 0
    for ci, cj in got:
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj            
            if 0 > min(ni, nj) or ni >= n or nj >= m:
                outer += 1
            elif not (ni, nj) in got:
                outer += 1
    #print(area, outer)
    return area * outer
ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            ans += go(i, j)

print(ans)