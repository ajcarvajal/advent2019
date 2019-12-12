def part1():
    total = 0
    for i in range(246540, 787419):
        x = str(i)
        dupe = False

        for i in range(0, len(x)-1):
            if x[i] == x[i+1]:
                if x.count(x[i]) == 2:
                    dupe = True

        if x == ''.join(sorted(x)) and dupe:
            total += 1

    return total


def part2():
    pass



print("\n____Part 1____")
print(part1())
print("\n____Part 2____")
print(part2())
