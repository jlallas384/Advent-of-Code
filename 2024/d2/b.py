ans = 0
try:
    while True:
        b = list(map(int, input().split()))
        has = 0
        for i in range(len(b)):
            a = b[:i] + b[i + 1:]
            n = len(a)
            if (all(a[i] < a[i + 1] for i in range(n - 1)) or all(a[i] > a[i + 1] for i in range(n - 1))) and all(abs(a[i] - a[i + 1]) <= 3 and abs(a[i] - a[i + 1]) >= 1 for i in range(n - 1)):
                has = 1
        a = b[:]
        n = len(a)
        if (all(a[i] < a[i + 1] for i in range(n - 1)) or all(a[i] > a[i + 1] for i in range(n - 1))) and all(abs(a[i] - a[i + 1]) <= 3 and abs(a[i] - a[i + 1]) >= 1 for i in range(n - 1)):
            has = 1
                               

        ans += has
except EOFError:
    pass
print(ans)