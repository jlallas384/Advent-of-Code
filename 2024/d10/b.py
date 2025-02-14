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
    q.append((i, j, 0))
    ret = 0
    while len(q):
        ci, cj, at = q.pop()
        if at == 9 :
            if g[ci][cj] == '9':
                ret += 1
            continue
        cur = int(g[ci][cj])
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if min(ni, nj) >= 0 and ni < n and nj < m and str(cur + 1) == g[ni][nj]:
                q.append((ni, nj, at + 1))
    return ret

for i in range(n):
    for j in range(m):
        if g[i][j] == '0':
            ans += go(i, j)
print(ans)