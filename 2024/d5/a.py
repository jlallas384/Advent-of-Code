from collections import defaultdict

graph = defaultdict(list)

while True:
    s = input().strip()
    if s == "":
        break
    x,y = map(int, s.split('|'))
    graph[y].append(x)

ans = 0
while True:
    try:
        a = list(map(int, input().split(',')))
        ok = 1
        vis = defaultdict(int)
        for i in range(len(a)):
            x = a[i]
            if any(vis[u] == 0 and u in a[i + 1:] for u in graph[x]):
                ok = 0
            vis[x] = 1
        if ok:
            ans += a[len(a) // 2]
    except EOFError:
        break

print(ans)

