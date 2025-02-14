g = []
while True:
    s = input().strip()
    if s == "":
        break
    g.append(list(s))

mvs = ""
while True:
    try:
        s = input()
        mvs += s
    except EOFError:
        break

n = len(g)
m = len(g[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dirc = "^>v<"

for i in range(n):
    for j in range(m):
        if g[i][j] == '@':
            ci, cj = i, j

for c in map(lambda x: dirc.index(x), mvs):
    di, dj = dirs[c]
    ni, nj = ci + di, cj + dj
    while g[ni][nj] == 'O':
        ni += di
        nj += dj
    if g[ni][nj] == '.':
        while (ni, nj) != (ci, cj):
            g[ni][nj] = g[ni - di][nj - dj]
            ni -= di
            nj -= dj
        g[ci][cj] = '.'
        ci, cj = ci + di, cj + dj

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 'O':
            ans += i * 100 + j
print(ans)