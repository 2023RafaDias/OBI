import numpy as np

size = int(input())
array = input()
pal = array.split()
res = [eval(i) for i in pal]

def palindrome(n,s,e,moves):

    if s == e:
        print(moves)
        return True

    
    if n[s] == n[e]:
        if e-s+1>2:
            return palindrome(n,s+1,e-1,moves)
            
        else:
            print(moves)
            return moves
            
        

    
    while n[s]!= n[e]:

        hold = e
        while n[s]>n[e]:
            n[e] = n[e]+n[e-1]
            np.delete(n,e-1)
            n.pop(e-1)
            e = e-1
            moves+=1

        while n[e]>n[s]:
            n[s] = n[s]+n[s+1]
            n.pop(s+1)
            moves+= 1
            e = e -1



    
    palindrome(n,s+1,e-1,moves)

palindrome(res,0,size-1,0)

    


        
