X = input()
X = X.split()

count = 0

yes = []
no = []

strike = []

for i in range(0,int(X[1])):
    Y = input()
    Y = Y.replace(" ","")
    strike.append(0)
    yes.append(Y)

for i in range(0,int(X[2])):
    Y = input()
    Y = Y.replace(" ","")
    no.append(Y)

for i in range(0,int(int(X[0])/3)):
    Z = input()
    Z = Z.replace(" ","")

    for j in range(0,len(no)):
        if no[j][0] in Z and no[j][1] in Z:
            count+= 1

    for j in range(0,len(yes)):
        if yes[j][0] in Z and not(yes[j][1] in Z):
            strike[j] += 1

for i in range(0,len(yes)):
    if strike[i] > 0:
        count+= 1

print(count)
