import fileinput

with fileinput.input() as f:
    for line in f:
        arg = [int(x) for x in line.strip()]

n = len(arg)
w = 25
h = 6


layers = list()


k = 0
while k < n:
   a = []
   for i in range(w*h):
       a.append(int(arg[k+i]))
   layers.append(a)
   k += w*h
   print(a)

nl = len(layers)
best = min(range(nl), key = lambda j: layers[j].count(0))
print("best:" ,layers[best].count(1) * layers[best].count(2))
print("count1: ", layers[best].count(1))
print("count2: ", layers[best].count(2))
print(layers[best])

count1 = 0
count2 = 0
for num in layers[best]:
    if num == 1:
        count1 +=1
    if num ==2 :
        count2 +=1
print(count1 * count2)





image = []


for i in range(w*h):
   k = 0
   while layers[k][i] == 2:
       k += 1
   image.append(layers[k][i])

for k in range(h):
   a = str()
   for cc in image[k*w:(k+1)*w]:
       if cc:
           a += '*'
       else:
           a += ' '
   print(a)
