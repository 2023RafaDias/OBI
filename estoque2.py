estoque = input()
estoque = estoque.split()

sizes = []
types = []
total = 0

for i in range(0,int(estoque[1])):
    sizes.append(0)

for i in range(0,int(estoque[0])):
    types.append(sizes.copy())

for i in range(0,int(estoque[0])):

    X = ""
    X = input()
    X = X.split()
        
    for j in range(0,int(estoque[1])):
        
        types[i][j] = int(X[j])
        
P = 0
while P<1 or P > 1000:
    P = int(input())

for i in range(0,P):

    enter = 1
    k = 0
    
    while enter != 0 and k != 2:
        enter = 0
        X = input()
        X = X.split()

        k+= 1
    
    if types[int(X[0])-1][int(X[1])-1] > 0:
        types[int(X[0])-1][int(X[1])-1] += -1
        total += 1
        
print(total)

