eqs = []

while True:
    try:
        s = input()
        s = s.split(": ")
        eqs.append((int(s[0]), list(map(int, s[1].split()))))
    except EOFError:
        break

ans = 0

for to, eq in eqs:
    ok = 0
    #print(to, eq)
    for msk in range(2 ** (len(eq) - 1)):
        p = eq[0]
        for bit in range(len(eq) - 1):
            if msk & (1 << bit):
                p += eq[bit + 1]
            else:
                p *= eq[bit + 1]
        if p == to:
            ok = 1
    ans += ok * to
print(ans)

