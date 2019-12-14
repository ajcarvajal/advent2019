import fileinput
from Computer import Computer
from collections import defaultdict

with fileinput.input() as f:
    for line in f:
        DATA = [int(x) for x in line.split(',')]

dirmap = {'UP':      ['LEFT','RIGHT'],
          'LEFT':    ['DOWN','UP'],
          'RIGHT':   ['UP', 'DOWN'],
          'DOWN':    ['RIGHT', 'LEFT']}

def day11():
    cpu = Computer(DATA, 1)
    grid = defaultdict(int)
    uniques = set()
    xpos = ypos = 0
    orientation = 'UP'
    while cpu.running:
        color = cpu.run()
        movedir = cpu.run()

        if color is None or movedir is None:
            break

        grid[(xpos,ypos)] = color
        uniques.add((xpos,ypos))

        #get next direction
        orientation = dirmap[orientation][movedir]

        #move to next spot
        if orientation == 'UP':
            ypos += 1
        elif orientation == 'LEFT':
            xpos -= 1
        elif orientation == 'RIGHT':
            xpos += 1
        elif orientation == 'DOWN':
            ypos -= 1

        cpu.inputs.append(grid[(xpos,ypos)])


    miny = min(uniques, key=lambda x: x[1])[1]
    maxy = max(uniques, key=lambda x: x[1])[1]
    minx = min(uniques, key=lambda x: x[0])[0]
    maxx = max(uniques, key=lambda x: x[0])[0]
    rowstr = ""
    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx+1):
            if grid[(x,y)] == 0:
                rowstr = rowstr + '.'
            else:
                rowstr = rowstr + '#'
        print(rowstr)
        rowstr = ""

    return len(uniques)


print(day11())

