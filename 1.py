import fileinput

data = [line.strip() for line in fileinput.input()]

def part1():
    total = 0
    for line in data:
        total += (int(line) // 3) - 2
    return total

def part2():
    total = 0
    for line in data:
        fuel = int(line)
        while fuel > 0:
            new = (fuel // 3) - 2
            if new > 0:
                total += new
                fuel = new
            else:
                break

    return total


print(part1())
print(part2())
