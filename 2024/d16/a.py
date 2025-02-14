import heapq

g = []

while True:
    try:
        g.append(input())
    except EOFError:
        break

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n = len(g)
m = len(g[0])
dist = [[[10**9] * 4 for j in range(m)] for i in range(n)]


pq = []

dist[n - 2][1][1] = 0
heapq.heappush(pq, (0, 1, (n - 2, 1)))

while len(pq):
    cdist, direction, (ci, cj) = heapq.heappop(pq)
    if cdist != dist[ci][cj][direction]:
        continue
    ni, nj = ci + dirs[direction][0], cj + dirs[direction][1]
    if 0 <= min(ni, nj) and ni < n and nj < m and g[ni][nj] != '#':
        if dist[ni][nj][direction] > cdist + 1:
            dist[ni][nj][direction] = cdist + 1
            heapq.heappush(pq, (dist[ni][nj][direction], direction, (ni, nj)))
    for d in [-1, 1]:
        if dist[ci][cj][(direction + d) % 4] > cdist + 1000:
            dist[ci][cj][(direction + d) % 4] = cdist + 1000
            heapq.heappush(pq, (dist[ci][cj][(direction + d) % 4], (direction + d) % 4, (ci, cj)))

print(min(dist[1][m - 2]))