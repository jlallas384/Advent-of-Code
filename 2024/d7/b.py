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
    for msk in range(3 ** (len(eq) - 1)):
        p = eq[0]
        cmsk = msk
        for bit in range(len(eq) - 1):
            if cmsk % 3 == 0:
                p += eq[bit + 1]
            elif cmsk % 3 == 1:
                p *= eq[bit + 1]
            else:
                p = int(str(p) + str(eq[bit + 1]))
            cmsk //= 3
            if p > to:
                break
        if p == to:
            ok = 1
    ans += ok * to
print(ans)