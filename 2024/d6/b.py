
import copy
ng = []
while True:
    try:
        s = input()
        ng.append(list(s))
    except EOFError:
        break

n = len(ng)
m = len(ng[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur = 0

for i in range(n):
    for j in range(m):
        if ng[i][j] == '^':
            cci, ccj = i, j

ans = 0
for i in range(n):
    for j in range(m):
        if ng[i][j] == '.':
            g = copy.deepcopy(ng)
            g[i][j] = '#'
            ok = 0
            s = set()
            ci, cj = cci, ccj
            cur = 0
            while 0 <= min(ci, cj) and ci < n and cj < m:
                if (ci, cj, cur) in s:
                    ok = 1
                    break
                s.add((ci, cj, cur))
                ni, nj = ci + dirs[cur][0], cj + dirs[cur][1]
                if 0 <= min(ni, nj) and ni < n and nj < m and g[ni][nj] == '#':
                    cur = (cur + 1) % 4
                else:
                    ci, cj = ni, nj
            ans += ok
print(ans)
                