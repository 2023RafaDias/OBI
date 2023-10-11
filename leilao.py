lances = []
N = -1
while N < 0 or N > 10000:
    N = int(input())

if N > 0:

    largest = 0
    person = "R"
    for i in range(0,2*N):
        if (i % 2) == 0:
            C = ""
            while len(C) > 10 or len(C) < 1:
                C = input()
            lances.append(C)
            
        else:
            V = 0
            while V < 1 or V > 100000:
                V = int(input())
            lances.append(V)
            if V > largest:
                largest = V
                person = lances[i-1]

    print(person)
    print(largest)

            


            
