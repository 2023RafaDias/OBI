import numpy

pal = input()
pal = pal.split()
res = [eval(i) for i in pal]

print(len(res))

nodes= []

for i in range(0,res[0]):
    nodes.append([])
    

print(nodes)


for i in range(0,res[1]):
    route = input()
    route = route.split()
    print(route)
    nodes[int(route[0])].append(route[1])
    nodes[int(route[0])].append(route[2])

print(nodes)

    
    
