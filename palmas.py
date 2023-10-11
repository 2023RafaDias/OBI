N = int(input())
I = int(input())
P = int(input())


if N >= 3 and N<= 100 and I >= 1 and I<= N and P >= 1 and P <= 1000:

    P = P % N
    
    if P > N-I:
        position = I + P - N
    else:
        position = I+P

    print(position)
