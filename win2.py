first = 1
second = 1
f = 0
s = 0

for i in range(0,5):
    x = int(input())

    if x > first:
        s = f
        f = 1
        second = first
        first = x
        
    elif x == first:
        f+= 1
    elif x > second:
        s = 1
        second = x
    elif x == second:
        s+=1

print(f,s)
        
    
        

    
