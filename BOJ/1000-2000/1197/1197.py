import sys


def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


V, E = map(int, input().split())
answer = 0
parent = [i for i in range(V+1)]
edge = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append([a, b, c])

edge.sort(key=lambda x: x[2])

for e in edge:
    if getParent(parent, e[0]) != getParent(parent, e[1]):
        union(parent, e[0], e[1])
        answer += e[2]

print(answer)
