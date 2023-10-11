E = input().split()
term = int(E[0])

add = 0
index = 0

for i in range(1,term+1):
    add = add + i*i
    if add >= term or add + (i+1)*(i+1) > term:
        index = i
        add = add - i*i
        break

print(index)

    
def pyramid(index):
    if index == 1:
        return 1
    else:
        return pyramid(index-1) + 1

print(pyramid(index))
        

def getIndex(term, add):
    for i in range(1,term+1):
        add = add + i*i
        if add >= term or add + (i+1)*(i+1) > term:
            add = term - add
            both = [add,i]
            print(both)
            return both
    

#def pyramid(index):
 #   if index ==1:
  #      return 1
   # elif 
    #    remainder = index*index
     #   getIndex(remainder,0)
        
        


def organise(term, sequence):
    if term == 0:
        return sequence
    else:
        both = getIndex(term,0)
        term = term - both[0]
        print(term)
        index = both[1]
        sequence.append(index)
        organise(term, sequence)

print(organise(5,[]))


    
    


    
