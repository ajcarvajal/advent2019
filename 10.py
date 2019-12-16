import fileinput
import math
import collections

DATA = [line.strip() for line in fileinput.input()]


def run():
    asteroids = list()
    angles = dict()
    angles2 = dict()
    for y, line in enumerate(DATA):
        for x, entity in enumerate(line):
            if entity == "#":
                angles[(x,y)] = set()
                angles2[(x,y)] = list()
                asteroids.append((x, y))

    for x1,y1 in asteroids:
        for x2, y2 in asteroids:
            angle = math.atan2(y2-y1, x2-x1)
            angles[(x1,y1)].add(angle)
            angles2[(x1,y1)].append((x2,y2))

    current = 0
    best = 0
    station = 0
    for k, v in angles.items():
        current = len(v)
        if current > best:
            station = k
            best = current

    print(best)

    ## part 2
    #angles2 = collections.OrderedDict(sorted(angles2.items()))
    #for k,v in angles2.items():
    #    v.sort()

    print(station)
    print(angles2[station][199])

run()
