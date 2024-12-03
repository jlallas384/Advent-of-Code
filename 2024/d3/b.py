import re

ans = 0
enable = 1
while True:
    try:
        s = input()
    except EOFError:
        break

    matches = re.finditer(r"mul\(\d{1,3}\,\d{1,3}\)", s)
    dos = list(re.finditer(r"do(n't)?\(\)", s))
    print(dos)

    for x in matches:
        while len(dos) and dos[0].end() <= x.start():
            enable = dos[0].group(0) == 'do()'
            dos.pop(0)
        x = x.group(0)
        t = x[4:-1]
        a,b = map(int, t.split(','))
        if enable:
            ans += a * b
print(ans)