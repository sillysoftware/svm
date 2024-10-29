r = [0] * 15
registers = {
    "rax": 0, "rbx": 1, "rcx": 2, "rdx": 3, "rdi": 4, "rsi": 5,
    "r8": 6, "r9": 7, "r10": 8, "r11": 9, "r12": 10, "r13": 11,
    "r14": 12, "r15": 13, "rsp": 14
}


def exec_mov(reg, value):
    if value[0] == "r":
        r[registers[reg]] = r[registers[value]]
    elif reg in registers:
        r[registers[reg]] = int(value)
    else:
        print("Error: Unknown register")


def exec_dump(reg):
    if reg in registers:
        print(f"{reg} = {r[registers[reg]]}")
    else:
        print("Error: Unknown register")


def exec_core_dump():
    for reg, index in registers.items():
        print(f"{reg} = {r[index]}")


def exec_xor(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] ^ r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_and(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] & r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_or(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] | r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_not(reg):
    if reg in registers:
        r[registers[reg]] = ~r[registers[reg]]
    else:
        print("Error: Unknown register")


def exec_nop():
    return


def exec_add(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] + r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_sub(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] - r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_mul(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] * r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_div(reg, reg1):
    if reg in registers and reg1 in registers:
        r[registers[reg]] = r[registers[reg]] / r[registers[reg1]]
    else:
        print("Error: Unknown register")


def exec_inc(reg):
    if reg in registers:
        r[registers[reg]] = r[registers[reg]] + 1
    else:
        print("Error: Unknown register")


def exec_dec(reg):
    if reg in registers:
        r[registers[reg]] = r[registers[reg]] - 1
    else:
        print("Error: Unknown register")

def exec_syscall():
    print("Calling the system")


operations = {
    "mov": lambda tokens: exec_mov(tokens[1], tokens[2]),
    "dump": lambda tokens: exec_dump(tokens[1]),
    "coredump": lambda tokens: exec_core_dump(),
    "xor": lambda tokens: exec_xor(tokens[1], tokens[2]),
    "and": lambda tokens: exec_and(tokens[1], tokens[2]),
    "or": lambda tokens: exec_or(tokens[1], tokens[2]),
    "not": lambda tokens: exec_not(tokens[1]),
    "nop": lambda tokens: exec_nop(),
    "add": lambda tokens: exec_add(tokens[1], tokens[2]),
    "sub": lambda tokens: exec_sub(tokens[1], tokens[2]),
    "mul": lambda tokens: exec_mul(tokens[1], tokens[2]),
    "div": lambda tokens: exec_div(tokens[1], tokens[2]),
    "inc": lambda tokens: exec_inc(tokens[1]),
    "dec": lambda tokens: exec_dec(tokens[1]),
    "syscall": lambda tokens: exec_syscall(),
}


def g():
    while True:
        source = input("(svm) >> ")
        tokens = [token.strip(",") for token in source.split()]
        command = tokens[0]
        if command == "exit":
            print("exit.")
            break
        elif command in operations:
            try:
                operations[command](tokens)
            except (IndexError, ValueError):
                print("Error: Invalid syntax")
        else:
            print("Error: Unknown command")


def main():
    g()


main()
