import fileinput
from collections import defaultdict

data = [line.strip() for line in fileinput.input()]

data = ['COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
        'K)YOU',
        'I)SAN']

def part1():
    orbits = dict()

    for line in data:
        orbitee, orbiter = line.split(')')
        orbits[orbiter] = orbitee

    total = 0
    for k in orbits:
        current = k
        while current in orbits:
            total += 1
            current = orbits[current]
    print(total)

    you = set(search(orbits, "YOU"))
    santa = set(search(orbits, "SAN"))
    print(len(you^santa))


def search(data, name):
    if data[name] in data:
        return [data[name]]+search(data, data[name])
    return []




part1()
