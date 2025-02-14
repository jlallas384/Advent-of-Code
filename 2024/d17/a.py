regs = [0] * 3

for i in range(3):
    s = input().split(": ")
    regs[i] = int(s[1])

input()

ins = list(map(int, input().split(": ")[1].split(",")))


ip = 0

def get_op(is_combo):
    if not is_combo:
        return ins[ip + 1]
    return ins[ip + 1] if ins[ip + 1] <= 3 else regs[ins[ip + 1] - 4]

while ip < len(ins):
    match ins[ip]:
        case 0:
            regs[0] //= 2 ** get_op(True)
            ip += 2
        case 1:
            regs[1] ^= get_op(False)
            ip += 2
        case 2:
            regs[1] = get_op(True) % 8
            ip += 2
        case 3:
            if regs[0]:
                ip = get_op(False)
            else:
                ip += 2
        case 4:
            regs[1] ^= regs[2]
            ip += 2
        case 5:
            print(get_op(True) % 8, end=',')
            ip += 2
        case 6:
            regs[1] = regs[0] // 2 ** get_op(True)
            ip += 2
        case 7:
            regs[2] = regs[0] // 2 ** get_op(True)            
            ip += 2    