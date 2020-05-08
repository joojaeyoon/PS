from itertools import permutations
from sys import maxsize

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

min_cost = maxsize

for perm in permutations([i for i in range(N)]):

    cost = 0

    flag = True

    for i in range(len(perm)-1):
        if costs[perm[i]][perm[i+1]] == 0:
            flag = False
            break
        cost += costs[perm[i]][perm[i+1]]
    if costs[perm[-1]][perm[0]] == 0:
        flag = False
    cost += costs[perm[-1]][perm[0]]

    if flag:
        min_cost = min(min_cost, cost)

print(min_cost)

# N = int(input())

# costs = [list(map(int, input().split())) for _ in range(N)]

# visited = [False for _ in range(N)]

# values = []


# def tsp(now, sumVal, first):

#     global values

#     if sum(visited) == N:
#         sumVal += costs[now][first]
#         values.append(sumVal)
#         return

#     for i in range(N):
#         if costs[now][i] != 0 and not visited[i]:
#             visited[i] = True
#             tsp(i, sumVal+costs[now][i], first)
#             visited[i] = False


# for i in range(N):
#     visited[i] = True
#     tsp(i, 0, i)
#     visited[i] = False

# print(min(values))
