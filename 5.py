import fileinput
from itertools import permutations
from Computer import Computer

with fileinput.input() as f:
    for line in f:
        MEMORY = [int(x) for x in line.split(',')]


def part1():
    cpu = Computer(MEMORY, 1)
    while cpu.running:
        cpu.run()

    return cpu.outputs[-1]

def part2():
    cpu = Computer(MEMORY, 5)
    cpu.run()
    return cpu.outputs[-1]

print(part1())
print(part2())
