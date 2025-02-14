g = []
sub = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.'
}

import copy
while True:
    s = input().strip()
    if s == "":
        break
    g.append(list(''.join(sub[x] for x in s)))

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
    path = []
    def dfs(ai, aj):
        if (ai, aj) in path:
            return False
        if g[ai][aj] == '.':
            return False
        if g[ai][aj] == '#':
            return True
        path.append((ai, aj))
        fail = False
        if g[ai][aj] == '[' and g[ai][aj + 1] == ']':
            fail |= dfs(ai, aj + 1)
        if g[ai][aj] == ']' and g[ai][aj - 1] == '[':
            fail |= dfs(ai, aj - 1)
        fail |= dfs(ai + di, aj + dj)
        return fail
    if not dfs(ci, cj):
        ng = copy.deepcopy(g)
        for i, j in path:
            ng[i][j] = '.'
        for i, j in path:
            ng[i + di][j + dj] = g[i][j]
        g = ng
        g[ni][nj] = '@'
        g[ci][cj] = '.'
        ci, cj = ni, nj

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '[':
            ans += i * 100 + j
print(ans)