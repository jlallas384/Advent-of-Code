#include <iostream>
#include <vector>
#include <sstream>

std::vector<int> oregs = {63281501, 0, 0};
std::vector<int> ins = {2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0};

int get_op(const std::vector<int>& ins, std::vector<int>& regs, int ip, bool is_combo) {
    if (!is_combo) {
        return ins[ip + 1];
    }
    return (ins[ip + 1] <= 3) ? ins[ip + 1] : regs[ins[ip + 1] - 4];
}

bool try_at(long long a_val) {
    std::vector<int> regs = oregs;
    regs[0] = a_val;
    int ip = 0;
    std::vector<int> cur;

    while (ip < ins.size() && cur.size() < ins.size()) {
        if (ins[ip] == 0) {
            regs[0] /= (1 << get_op(ins, regs, ip, true));
            ip += 2;
        } else if (ins[ip] == 1) {
            regs[1] ^= get_op(ins, regs, ip, false);
            ip += 2;
        } else if (ins[ip] == 2) {
            regs[1] = get_op(ins, regs, ip, true) % 8;
            ip += 2;
        } else if (ins[ip] == 3) {
            if (regs[0]) {
                ip = get_op(ins, regs, ip, false);
            } else {
                ip += 2;
            }
        } else if (ins[ip] == 4) {
            regs[1] ^= regs[2];
            ip += 2;
        } else if (ins[ip] == 5) {
            cur.push_back(get_op(ins, regs, ip, true) % 8);
            if (cur.back() != ins[cur.size() - 1]) {
                return false;
            }
            ip += 2;
        } else if (ins[ip] == 6) {
            regs[1] = regs[0] / (1 << get_op(ins, regs, ip, true));
            ip += 2;
        } else if (ins[ip] == 7) {
            regs[2] = regs[0] / (1 << get_op(ins, regs, ip, true));
            ip += 2;
        }
    }
    return cur.size() == ins.size();
}

int main() {
    for (long long i = 0; i < 100000000000LL; ++i) {
        if (try_at(i)) {
            std::cout << i << std::endl;
            break;
        }
    }

    return 0;
}
