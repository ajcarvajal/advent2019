import fileinput
from random import randint
from collections import namedtuple, defaultdict


lines = fileinput.input()
inputs = [[n for n in line.split(',')] for line in lines ]
inputs = [[(n[0], int(n[1:])) for n in input] for input in inputs]


dir_map = {
   'R': (1,0),
   'U': (0,1),
   'D': (0,-1),
   'L': (-1,0),
}


def tuple_mul(a, n):
   return tuple(x * n for x in a)


def tuple_add(a, b):
   return tuple(n[0] + n[1] for n in zip(a,b))


def man_dis(a):
   return abs(a[0]) + abs(a[1])


line = {}
intersections = set()
pos = (0,0)
step_count = 0


for path in inputs[0]:
   steps = [tuple_mul(dir_map[path[0]], n) for n in range(1, path[1]+1)]
   for step in steps:
       target_pos = tuple_add(pos, step)
       step_count += 1
       line[target_pos] = min(step_count, line.get(target_pos, 1e20))

   pos = tuple_add(pos, steps[-1])


pos = (0,0)
step_count = 0
line2 = {}
for path in inputs[1]:
   steps = [tuple_mul(dir_map[path[0]], n) for n in range(1, path[1]+1)]
   for step in steps:
       target_pos = tuple_add(pos, step)
       step_count += 1
       line2[target_pos] = min(step_count, line2.get(target_pos, 1e20))
       if target_pos in line:
           intersections.add(target_pos)


   pos = tuple_add(pos, steps[-1])


# print (intersections)
# print (len(intersections))


answer1 = min([man_dis(inter) for inter in intersections])
print (answer1)




answer2 = min(line[n] + line2[n] for n in intersections)
print(answer2)
