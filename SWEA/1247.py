T = int(input())

min_cost = 100000000


def find(x, y, cost, visited, pos, N, end):

    if visited == (1 << N)-1:
        global min_cost
        cost += abs(x-end[0])+abs(y-end[1])
        min_cost = min(cost, min_cost)
        return

    for i in range(N):
        if not visited & (1 << i):
            visited |= (1 << i)
            d = abs(x-pos[i][0])+abs(y-pos[i][1])
            find(pos[i][0], pos[i][1], cost+d, visited, pos, N, end)
            visited &= ~(1 << i)


for i in range(T):
    N = int(input())

    tmp = list(map(int, input().split()))

    pos = []

    for j in range(0, len(tmp), 2):
        pos.append([tmp[j], tmp[j+1]])

    start = pos[0]
    end = pos[1]

    pos = pos[2:]

    find(start[0], start[1], 0, 0, pos, N, end)

    print(f"#{i+1} {min_cost}")

    min_cost = 1000000
