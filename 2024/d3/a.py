import re

ans = 0
while True:
    try:
        s = input()
    except EOFError:
        break

    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", s)

    for x in matches:
        t = x[4:-1]
        a,b = map(int, t.split(','))
        ans += a * b
print(ans)