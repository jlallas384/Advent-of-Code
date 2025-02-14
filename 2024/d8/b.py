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
            if a1 == a2:
                continue
            dy = a2[0] - a1[0]
            dx = a2[1] - a1[1]
            i = a2[0] + dy
            j = a2[1] + dx
            s.add((a2[0], a2[1]))
            while min(i, j) >= 0 and i < n and j < m:
                s.add((i, j))

                i += dy
                j += dx
print(len(set(s)))