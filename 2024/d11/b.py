import functools
a = list(map(int, input().split()))

@functools.lru_cache()
def f(x, i):
    print(x,)
    if i == 0:
        return 1
    if x == 0:
        return f(1, i - 1)
    if len(str(x)) % 2 == 0:
        g = str(x)
        return f(int(g[:len(g) // 2]), i - 1) + f(int(g[len(g) // 2:]), i - 1)
    return f(x * 2024, i - 1)

print(functools.reduce(lambda x, y: x + y, [f(x, 25) for x in a]))