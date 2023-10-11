X = input().split()

term = int(X[0])

m = int(X[1])

def getIndex(term, add):
    for i in range(1,term+1):
        add = add + i*i
        if add >= term or add + (i+1)*(i+1) > term:
            add = term - add
            both = [add,i]
            return both

def undoPyramid(index, order, count, i, m, p):
    remainder = index*index
    n = order[i]
    order[i] = n-1
    sequence(remainder,order,count, m, p)



def sequence(term, order, count, m, p):
    if term == 0:
        indexes = []
        total = []

        
        
        for i in range(0,len(order)):
            if order[i] not in indexes:
                indexes.append(order[i])
                total.append(0)
                
                for j in range(0,len(order)):
                    if order[i] == order[j]:
                        total[i]+= 1

        mult = 1
        for i in range(1,len(order)+1):
            mult = mult*i

        temp = 1
        for i in range(0,len(total)):
            for j in range(1,total[i]+1):
                temp = temp*j
            
        mult = mult/temp
    

            
        count = count + mult

        


        
        if m == 2:
            return 1
            
        for i in range(0,len(order)):
            if not(order[i]==1):
                undoPyramid(order[i],order,count,i, m, p)


        if p == 0:
            print(count)
            p += 1
        


        
        

        return 1
    else:
        both = getIndex(term,0)

        term = both[0]
        index = both[1]
        order.append(index)

        sequence(term,order,count,m, p)


print(sequence(term,[],0,m,0))
