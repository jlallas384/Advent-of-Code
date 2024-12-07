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
cur = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == '^':
            ci, cj = i, j

s = set()

while 0 <= min(ci, cj) and ci < n and cj < m:
    s.add((ci, cj))
    ni, nj = ci + dirs[cur][0], cj + dirs[cur][1]
    if 0 <= min(ni, nj) and ni < n and nj < m and g[ni][nj] == '#':
        cur = (cur + 1) % 4
    else:
        ci, cj = ni, nj
print(len(set(s)))
    