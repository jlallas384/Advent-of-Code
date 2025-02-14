cs = []


while True:
    try:
        s = input()
        cs.append(tuple(map(int, s.split(","))))
    except EOFError:
        break

n, m = 71, 71

g = [[-1] * m for i in range(n)]


q = [(0, 0)]
g[0][0] = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while len(q):
    ci, cj = q.pop(0)
    for di, dj in dirs:
        ni, nj = ci + di, cj + dj
        if 0 <= min(ni, nj) and ni < n and nj < m and (ni, nj) not in cs[:1024] and g[ni][nj] == -1:
            g[ni][nj] = g[ci][cj] + 1
            q.append((ni, nj))
print(g[-1][-1])