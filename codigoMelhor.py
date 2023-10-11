from collections import Counter

X = input().split()
N = int(X[0])
M = int(X[1])
K = int(X[2])

yes = set(input().replace(" ", "") for _ in range(M))
no = set(input().replace(" ", "") for _ in range(K))

count = 0
strike_counter = Counter()

for _ in range(N // 3):
    Z = input().replace(" ", "")
    for j in range(len(no)):
        if no[j][0] in Z and no[j][1] in Z:
            count += 1

    for j in range(len(yes)):
        if (yes[j][0] in Z and not yes[j][1] in Z) or (yes[j][1] in Z and not yes[j][0] in Z):
            strike_counter[j] += 1

for strike in strike_counter.values():
    if strike >= 2:
        count += 1

print(count)
