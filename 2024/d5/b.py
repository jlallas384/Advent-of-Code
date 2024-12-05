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
        if not ok:
            ts = []
            vis = defaultdict(int)
            def dfs(v):
                vis[v] = 1
                for u in graph[v]:
                    if u not in a:
                        continue
                    if vis[u] == 0:
                        dfs(u)
                    elif vis[u] == 1:
                        assert False
                vis[v] = 2
                ts.append(v)
            for x in a:
                if vis[x] == 0:
                    dfs(x)
            ans += ts[len(ts) // 2]
    except EOFError:
        break

print(ans)

