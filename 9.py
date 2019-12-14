import fileinput
from Computer import Computer

with fileinput.input() as f:
    for line in f:
        DATA = [int(x) for x in line.split(',')]

#DATA = [104,1125899906842624,99]
#DATA = [1102,34915192,34915192,7,4,7,99,0]
#DATA = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

def part1():
    cpu = Computer(DATA, 1)
    while cpu.running:
        cpu.run()
    return cpu.outputs


def part2():
    cpu = Computer(DATA, 2)
    while cpu.running:
        cpu.run()
    return cpu.outputs

print(part1())
print(part2())

