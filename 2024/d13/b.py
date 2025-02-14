from gekko import GEKKO
g = []

while True:
    try:
        f = lambda x: tuple(int(i[2:]) for i in x.split(": ")[1].split(", "))
        a = f(input())
        b = f(input())
        z = input()[7:].split(", ")
        c = tuple(int(x[2:]) + 10000000000000 * 0 for x in z)
        input()
        g.append((a, b, c))
    except EOFError:
        break

aa = 0
for (x1, y1), (x2, y2), (tx, ty) in g:
    m = GEKKO()

    a, b = m.Array(m.Var, 2, integer=True, lb=0)
    c = a * 3 + b
    m.Minimize(c)
    m.Equations([x1 * a + x2 * b == tx, y1 * a + y2 * b == ty])
    #m.options.SOLVER = 1
    try:
        m.solve(disp=False)
        aa += int(a.value[0] * 3 + b.value[0])
    except :
        pass
print(aa)