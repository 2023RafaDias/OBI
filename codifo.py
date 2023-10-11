size = int(input())
new = ''
current = input()
hold = current[0]

count = 1

print(current)

for i in range(1,size):
    
    if current[i] == hold:
        count += 1
    else:
        new = new + str(count)
        new = new + ' '
        new = new + hold
        new = new + ' '
        
        count = 1
        hold = current[i]

    if i == size-1:
        new = new + str(count)
        new = new + ' '
        new = new + hold
        new = new + ' '
           
print(new)
        
        
    
