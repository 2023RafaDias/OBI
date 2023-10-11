X = int(input())

hold = ['-1']

finalcount = 0
count = 0

word = ''

wait = 1
last = 1

for i in range(0,X):
    hold.append(input())

while wait <= X:

    if not(hold[wait] in word):
        word = word + hold[wait]
        wait += 1
        count+= 1
        
    else:
        last+= 1

        if finalcount < len(word):
            finalcount= len(word)

        if X-last > len(word):
            wait = last
        else:
            break

        word = ''
    
if finalcount < len(word):
    finalcount= len(word)

print(finalcount)

