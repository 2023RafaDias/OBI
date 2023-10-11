N = int(input())

workers = []
unhappy = []

hello = [0,1]

if 0 in hello:
    print("here")

first = input().split()

workers.append(first)

for i in range(1,N):
    L = input().split()
    workers.append(L)


    if workers[i][1]>workers[int(L[0])-1][1]:
        
        if not(workers[i][0]) in unhappy):
            unhappy.append(workers[i][0]))
            
print(len(unhappy))

unhappy = []

A = int(input())
for i in range(0,A):
    L = input().split()
    sub = int(L[0])-1
    high = int(workers[sub][0])-1
    
    workers[sub][1] = L[1]


    if workers[sub][1]>workers[high][1]:
        
        if not(int(workers[sub][0]) in unhappy):
            unhappy.append(int(workers[sub][0]))
            print(int(workers[sub][0]))

    
