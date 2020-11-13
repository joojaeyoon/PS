import sys

sys.setrecursionlimit(10**8)
G = int(input())
P = int(input())

gate = [i for i in range(G+1)]
airplane = [int(sys.stdin.readline()) for _ in range(P)]
answer = 0


def find(parent, x):
    if parent[x] == x:
        return x
    gate[x] = find(parent, parent[x])
    return gate[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for a in airplane:
    tmp = find(gate, a)

    if not tmp:
        break
    union(gate, tmp, tmp-1)
    answer += 1

print(answer)
