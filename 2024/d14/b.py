n,m = 103, 101
a0, a1, a2, a3 = 0, 0, 0, 0

midn = n // 2
midm = m // 2
a = []
while True:
    try:
        s = input().split()
        p = list(map(int, s[0][2:].split(',')))
        v = list(map(int, s[1][2:].split(',')))

        a.append((p, v))
    except EOFError:
        break



for x, y in a:
    print([x, y],',',sep='')