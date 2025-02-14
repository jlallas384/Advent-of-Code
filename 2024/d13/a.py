from functools import lru_cache
g = []

while True:
    try:
        f = lambda x: tuple(int(i[2:]) for i in x.split(": ")[1].split(", "))
        a = f(input())
        b = f(input())
        z = input()[7:].split(", ")
        c = tuple(int(x[2:]) for x in z)
        input()
        g.append((a, b, c))
        print(a, b, c)
    except EOFError:
        break
aa = 0
for a, b, (tx, ty) in g:
    it = 0
    has = 1e9
    while a[0] * it <= tx and a[1] * it <= ty:
        nd = (tx - a[0] * it) // b[0]
        if a[0] * it + b[0] * nd == tx and a[1] * it + b[1] * nd == ty:
            has = min(has, it * 3 + nd)
        it += 1
    if has < 1e9:
        aa += has
print(aa)