import sys


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

answer = 0
parent = [i for i in range(N+1)]

costs = []

for _ in range(M):
    costs.append(list(map(int, sys.stdin.readline().split())))

costs.sort(key=lambda x: x[2])

for cost in costs:
    a, b, c = cost

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += c

print(answer)
