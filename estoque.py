estoque = input()
estoque = estoque.split()

while int(estoque[0])<1 or int(estoque[0])>500 or int(estoque[1])<1 or int(estoque[1])>500:
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
    enter = 1
    k = 0
    
    while enter != 0 and k != int(estoque[1]) :
        enter = 0
        X = input()
        X = X.split()
        for j in range(0,int(estoque[1])):
            if int(X[j]) < 0 or int(X[j]) > 10:
                print(X[j])
                enter += 1
        k+= 1
        
    
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

        if int(X[0]) < 0 or int(X[0]) > int(estoque[0]):
            enter += 1
        if int(X[1]) < 0 or int(X[1]) > int(estoque[1]):
            enter += 1

        k+= 1
    
    if types[int(X[0])-1][int(X[1])-1] > 0:
        types[int(X[0])-1][int(X[1])-1] += -1
        total += 1
        
print(total)
