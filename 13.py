import fileinput
from collections import defaultdict
from Computer import Computer

with fileinput.input() as f:
    for line in f:
        DATA = [int(x) for x in line.split(',')]


def game():
    cpu = Computer(DATA, 0)

    def controls():
        x = input()
        if x == 'h':
            return -1
        if x == 'l':
            return 1
        return 0

    cpu.set_input_func(controls)
    cpu.memory[0] = 2
    output = None
    screen = defaultdict(int)
    while cpu.running:
        xpos = cpu.run()
        ypos = cpu.run()
        tile = cpu.run()

        if xpos is None or ypos is None:
            break
        screen[(xpos,ypos)] = tile
        subprocess.run('clear')
        draw(screen)

def draw(screen):
    miny = min(screen.keys(), key=lambda x: x[1])[1]
    maxy = max(screen.keys(), key=lambda x: x[1])[1]
    minx = min(screen.keys(), key=lambda x: x[0])[0]
    maxx = max(screen.keys(), key=lambda x: x[0])[0]
    rowstr = ""
    block_count = 0
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if x == -1 and y == 0:
                rowstr = rowstr + str(screen[(x,y)])
            else:
                if screen[(x,y)] == 0:
                    rowstr = rowstr + ' '
                elif screen[(x,y)] == 1:
                    rowstr = rowstr + '#'
                elif screen[(x,y)] == 2:
                    block_count +=1
                    rowstr = rowstr + 'B'
                elif screen[(x,y)] == 3:
                    rowstr = rowstr + '-'
                elif screen[(x,y)] == 4:
                    rowstr = rowstr + 'o'
        print(rowstr)
        rowstr = ""



game()
