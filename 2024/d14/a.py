n,m = 103, 101
a0, a1, a2, a3 = 0, 0, 0, 0

midn = n // 2
midm = m // 2

while True:
    try:
        s = input().split()
        p = list(map(int, s[0][2:].split(',')))
        v = list(map(int, s[1][2:].split(',')))
        p[0] = (p[0] + v[0] * 100) % m
        p[1] = (p[1] + v[1] * 100) % n
        x, y = p
        if x < midm and y < midn:
            a0 += 1
        elif x > midm and y < midn:
            a1 += 1
        elif x < midm and y > midn:
            a2 += 1
        elif x > midm and y > midn:
            a3 += 1
    except EOFError:
        break

print(a0 * a1 * a2 * a3)