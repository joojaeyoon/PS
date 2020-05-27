N = int(input())

T = []
P = []

cost = 0

for i in range(N):
    T.append(0)
    P.append(0)

    T[i], P[i] = map(int, input().split())


def find(day, total):
    global cost

    flag = True

    for i in range(day, N):
        if day+T[i]+i-day <= N:
            find(day+T[i]+i-day, total+P[i])
            flag = False

    if flag:
        cost = max(cost, total)
        return


find(0, 0)

print(cost)
