import fileinput
from itertools import permutations
from Computer import Computer

with fileinput.input() as f:
    for line in f:
        MEMORY = [int(x) for x in line.split(',')]


outputs = []
for sequence in permutations(range(5,10)):
    cluster = [Computer(MEMORY, phase) for phase in sequence]

    output = 0
    while True:
        for cpu in cluster:
            output = cpu.run(output)

        if cpu.running:
            outputs.append(output)
        else:
            break

#79846026
print(max(outputs))
