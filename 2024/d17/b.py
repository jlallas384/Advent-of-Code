oregs = [0] * 3

for i in range(3):
    s = input().split(": ")
    oregs[i] = int(s[1])

input()

ins = list(map(int, input().split(": ")[1].split(",")))



def try_at(a_val):
    regs = oregs[:]
    regs[0] = a_val
    def get_op(is_combo):
        if not is_combo:
            return ins[ip + 1]
        return ins[ip + 1] if ins[ip + 1] <= 3 else regs[ins[ip + 1] - 4]
    ip = 0
    cur = []
    while ip < len(ins) and len(cur) < len(ins):
        if ins[ip] == 0:
            regs[0] //= 2 ** get_op(True)
            ip += 2
        elif ins[ip] == 1:
            regs[1] ^= get_op(False)
            ip += 2
        elif ins[ip] == 2:
            regs[1] = get_op(True) % 8
            ip += 2
        elif ins[ip] == 3:
            if regs[0]:
                ip = get_op(False)
            else:
                ip += 2
        elif ins[ip] == 4:
            regs[1] ^= regs[2]
            ip += 2
        elif ins[ip] == 5:
            cur.append(get_op(True) % 8)
            ip += 2
        elif ins[ip] == 6:
            regs[1] = regs[0] // 2 ** get_op(True)
            ip += 2
        elif ins[ip] == 7:
            regs[2] = regs[0] // 2 ** get_op(True)
            ip += 2
    return len(cur) == len(ins), cur

for i in range(0, 10000000):
    f, g = try_at(i)
    print(f, g)
