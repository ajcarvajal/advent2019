import fileinput

with fileinput.input() as f:
    for line in f:
        MEMORY = [int(x) for x in line.split(',')]


def part1(memory, noun = 12, verb = 2):
    i = 0
    memory = MEMORY.copy()
    memory[1], memory[2] = noun, verb
    while memory[i] != 99:
        op, a, b, c = memory[i:i+4]
        if op == 1:
            memory[c] = memory[a] + memory[b]
        if op == 2:
            memory[c] = memory[a] * memory[b]
        i += 4
    return memory[0]


def part2():
    target = 19690720

    for noun in range(0, 99):
        for verb in range(0, 99):
            opcode = part1(MEMORY, noun, verb)
            if opcode == target:
                return 100 * noun + verb



print(part1(MEMORY))
print(part2())
