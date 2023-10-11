S = int(input())
A = int(input())
B = int(input())


add = 0

for i in range(A,B+1):
    total = 0
    
    m = str(i)
    
    for j in range(0,len(m)):
        total += int(m[j])

    if total == S:
        add+= 1

print(add)
