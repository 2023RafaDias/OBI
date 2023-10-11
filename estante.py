X = input()
X = X.split()

total = int(X[0]) + int(X[1]) + int(X[2])

sobrando = total % int(X[3])

print(sobrando)
