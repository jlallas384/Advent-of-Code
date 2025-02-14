from collections import deque
g = []
while True:
    try:
        s = input()
        g.append(list(s))
    except EOFError:
        break

n = len(g)
m = len(g[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]   

for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            si, sj = i, j
        if g[i][j] == 'E':
            ei, ej = i, j

def bfs():
    dst = [[-1] * m for i in range(n)]
    dst[si][sj] = 0
    q = deque()
    q.append((si, sj))

    while len(q):
        i, j = q.popleft()
        if (i, j) == (ei, ej):
            break
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= min(ni, nj) and ni < n and nj < m and g[ni][nj] != '#' and dst[ni][nj] == -1:
                dst[ni][nj] = dst[i][j] + 1
                q.append((ni, nj))
    return dst[ei][ej]


real = bfs()

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            g[i][j] = '.'
            new = bfs()
            g[i][j] = '#'
            if real - new >= 100:
                ans += 1

print(ans)