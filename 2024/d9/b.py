s = input()

a = []

free = []
at = 0
for i, x in enumerate(s):
    if i % 2 == 0:
        a.append((i // 2, int(x), at))
    else:
        free.append((at, int(x)))
    at += int(x)       

poses = []


for idd, ln, where in reversed(a):
    moved = 0
    for i in range(len(free)):
        tat, tln = free[i]
        if free[i][1] >= ln and tat < where:
            free = free[:i] + free[i+1:]
            if tln - ln:
                free.append((tat + ln, tln - ln))
                free.sort()
            moved = 1
            poses.append((tat, ln, idd))
            break
    if not moved:
        poses.append((where, ln, idd))

ans = 0
for pos, ln, idd in poses:
    for i in range(ln):
        ans += (pos + i) * idd
print(ans)