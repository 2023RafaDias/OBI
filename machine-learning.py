N = int(input())

topic = []
count = []
content = []


for i in range(0,N):
    S = input().split();
    topic.append(S[0])
    count.append(0)
    hold = []
    for i in range(0,int(S[1])):
        hold.append(S[i+2])

    content.append(hold.copy())

X = int(input())

text = input().split()

for i in range(0,X):
    for j in range(0,N):
        if text[i] in content[j]:
            count[j] += 1

index = 0
for i in range(0,len(count)):
    if count[i] > count[index]:
        index = i
    elif count[i] == count[index]:
        if topic[index][0] > topic[i][0]:
            index = i

print(topic[index])


    
