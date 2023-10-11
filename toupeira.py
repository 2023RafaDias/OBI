X = input()
X = X.split()

houses = []

for i in range(0,int(X[0])):
    houses.append([i+1])

for i in range(0,int(X[1])):
    Y = input()
    Y = Y.split()

    if int(Y[0]) not in houses:
           houses.append(Y[0])

    if int(Y[1]) not in houses:
           houses.append(Y[1])
           
    for j in range(0,int(X[0])):
        if int(Y[0]) == houses[j][0]:
            houses[j].append(int(Y[1]))

        if int(Y[1]) == houses[j][0]:
            houses[j].append(int(Y[0]))
    

P = int(input())
yes = 0
count = 0

for i in range(0,P):
    yes = 0
    Z = input()
    Z = Z.split()
    for j in range(1,len(Z)-1):
        if int(Z[j+1]) in houses[int(Z[j])-1]:
            yes += 1

        if yes == (int(Z[0])-1):
            count+= 1

print(count)
            
