import sys


def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
answer = 0
parent = [i for i in range(N+1)]

ways = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    ways.append((a, b, c))

ways.sort(key=lambda x: x[2])

last_cost = 0

for way in ways:
    a, b, c = way
    if getParent(parent, a) != getParent(parent, b):
        union(parent, a, b)
        answer += c
        last_cost = c

answer -= last_cost

print(answer)
