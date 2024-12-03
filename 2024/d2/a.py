ans = 0
try:
    while True:
        a = list(map(int, input().split()))
        n = len(a)
        if (all(a[i] < a[i + 1] for i in range(n - 1)) or all(a[i] > a[i + 1] for i in range(n - 1))) and all(abs(a[i] - a[i + 1]) <= 3 and abs(a[i] - a[i + 1]) >= 1 for i in range(n - 1)):
            ans += 1
except EOFError:
    pass
print(ans)