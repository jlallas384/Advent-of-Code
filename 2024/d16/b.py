from collections import deque

g = []

while True:
    try:
        g.append(input())
    except EOFError:
        break

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n = len(g)
m = len(g[0])


def bfs(si, sj, sdir):
    dist = [[[10**9] * 4 for j in range(m)] for i in range(n)]
    dist[si][sj][sdir] = 0
    pq = deque()
    pq.append((0, sdir, (si, sj)))
    while len(pq):
        cdist, direction, (ci, cj) = pq.popleft()
        if cdist != dist[ci][cj][direction]:
            continue
        ni, nj = ci + dirs[direction][0], cj + dirs[direction][1]
        if 0 <= min(ni, nj) and ni < n and nj < m and g[ni][nj] != '#':
            if dist[ni][nj][direction] > cdist + 1:
                dist[ni][nj][direction] = cdist + 1
                pq.appendleft((dist[ni][nj][direction], direction, (ni, nj)))
        for d in [-1, 1]:
            if dist[ci][cj][(direction + d) % 4] > cdist + 1000:
                dist[ci][cj][(direction + d) % 4] = cdist + 1000
                pq.append((dist[ci][cj][(direction + d) % 4], (direction + d) % 4, (ci, cj)))
    return dist


dist = bfs(n - 2, 1, 1)
shortest = min(dist[1][m - 2])

distends = [bfs(1, m - 2, k) for k in range(4)]
print(shortest)
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] != '#':
            if any(dist[i][j][k] + distends[l][i][j][k ^ 2] == shortest for k in range(4) for l in range(4)):
                ans += 1

print(ans)