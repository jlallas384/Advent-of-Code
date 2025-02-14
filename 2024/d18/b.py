cs = []


while True:
    try:
        s = input()
        cs.append(tuple(map(int, s.split(","))))
    except EOFError:
        break

n, m = 71, 71


def go(amount):
    g = [[-1] * m for i in range(n)]


    q = [(0, 0)]
    g[0][0] = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ccs = set(cs[:amount])
    while len(q):
        ci, cj = q.pop(0)
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= min(ni, nj) and ni < n and nj < m and (ni, nj) not in ccs and g[ni][nj] == -1:
                g[ni][nj] = g[ci][cj] + 1
                q.append((ni, nj))
    return g[-1][-1]

lo, hi = 1, len(cs)
ans = None
while lo <= hi:
    m = (lo + hi) // 2
    f = go(m)
    if f == -1:
        ans = cs[m - 1]
        hi = m - 1
    else:
        lo = m + 1

print(ans)