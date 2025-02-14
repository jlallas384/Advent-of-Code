s = input()

a = []

for i, x in enumerate(s):
    if i % 2 == 0:
        a = a + [i // 2] * int(x)
    else:
        a = a + [-1] * int(x)        

pt = 0

while -1 in a:
    while len(a) and a[-1] == -1:
        a.pop()
    if not len(a) or -1 not in a:
        break
    x = a.pop()
    while pt < len(a) and a[pt] != -1:
        pt += 1
    a[pt] = x

ans = 0
for i, x in enumerate(a):
    ans += i * int(x)
print(ans)