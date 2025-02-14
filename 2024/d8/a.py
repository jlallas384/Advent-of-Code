from collections import defaultdict
g = []

while True:
    try:
        s = input()
        g.append(s)
    except EOFError:
        break
n = len(g)
m = len(g[0])

s = set()
dct = defaultdict(list)
for i in range(n):
    for j in range(m):
        if g[i][j] != '.':
            dct[g[i][j]].append((i, j))

for x in dct.values():
    for a1 in x:
        for a2 in x:
            dy = a2[0] - a1[0]
            dx = a2[1] - a1[1]
            i = a2[0] + dy
            j = a2[1] + dx
            if min(i, j) >= 0 and i < n and j < m:
                if (i, j) != a1 and (i, j) != a2:
                    d1 = abs(i - a1[0]) + abs(j - a1[1])
                    d2 = abs(i - a2[0]) + abs(j - a2[1])
                    if d1 > d2:
                        d1, d2 = d2, d1
                        if d1 * 2 == d2:
                            s.add((i, j))
print(len(set(s)))