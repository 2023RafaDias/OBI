N = int(input())
workers = []
unhappy = []

salary = []

L = input().split()

workers.append([L[1]])

for i in range(1,N):
    L = input().split()
    salary.append(L)
    print(salary)
    workers.append([L[1]])
    workers[int(L[0])-1].append(L[1])

    if L[1]>workers[int(L[0])-1][0]:
        if not(workers[int(L[0])-1][0] in unhappy):
            unhappy.append(workers[int(L[0])-1][0])
        
    

print(workers)
print(len(unhappy))

unhappy = []

