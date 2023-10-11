total = 0
contas = [0,0,0]

V = -1
while V < 0 or V > 2000:
    V = int(input())

total = V

A = 0
F = 0
P = 0

while A < 1 or A > 1000:
    A = int(input())

while F < 1 or F > 1000:
    F = int(input())

while P < 1 or P > 1000:
    P = int(input())

contas[0] = A
contas[1] = F
contas[2] = P

contas = sorted(contas)

can = 0

for i in range(0,3):
    total += - contas[i]
    if total >= 0:
        can += 1
    else:
        break

print(can)
