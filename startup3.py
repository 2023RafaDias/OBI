N = int(input())
workers = []
unhappy = []

difference = []
biggest = []
sal = []

L = input().split()

workers.append([L[1]])

salary = []

salary.append(L[0])


for i in range(1,N):
    L = input().split()

    salary.append(L[0])
    workers.append([L[1]])
    
    workers[int(L[0])-1].append(L[1])

    if int(L[1])>int(workers[int(L[0])-1][0]):

        if not(int(L[0]) in unhappy):
            unhappy.append(int(L[0]))

    
print(len(unhappy))

for i in range(0,len(workers)):
    hold = int(workers[i][0])

    workers[i].sort()

    difference.append(int(workers[i][-1])-hold)
    sal.append(hold)
    biggest.append(int(workers[i][-1]))


A = int(input())

for i in range(0,A):
    L = input().split()

    if (int(L[1])- sal[int(L[0])-1]) >= difference[int(L[0])-1]:
        if int(L[0]) in unhappy:
            unhappy.remove(int(L[0]))

    store = sal[int(L[0])-1]

    sal[int(L[0])-1] = int(L[1])
    
    if int(L[1]) > sal[int(salary[int(L[0])-1])-1]:
        if not(int(salary[int(L[0])-1]) in unhappy):
            unhappy.append(int(salary[int(L[0])-1]))
            biggest[int(salary[int(L[0])-1])-1] = int(L[1])

    elif store == biggest[int(salary[int(L[0])-1])-1] and int(L[1]) < store:
        
        for j in range(1,len(workers[int(salary[int(L[0])-2])])+1):

            
            if int(workers[int(salary[int(L[0])-2])][-j])>sal[int(salary[int(L[0])-1])-1]:

                if not(int(salary[int(L[0])-1]) in unhappy):
                    unhappy.append(int(salary[int(L[0])-1]))
                    biggest[int(salary[int(L[0])-1])-1] = int(workers[int(salary[int(L[0])-2])][-j])

                else:

                    if int(L[0]) in unhappy:
                        unhappy.remove(int(L[0]))

                
        
     #   if int(salary[int(L[0])-1]) in unhappy:
      #      unhappy.remove(int(salary[int(L[0])-1]))

        

    sal[int(L[0])-1] = int(L[1])

    print(len(unhappy))

        
        

    


    



