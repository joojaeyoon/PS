import sys
from collections import Counter


def find(parent, x):
    if x == parent[x]:
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

parent = [i for i in range(N)]
pos = [[-1 for _ in range(1001)] for __ in range(1001)]


def check(x, y, n):
    if pos[y][x] != -1:
        union(parent, pos[y][x], n)
    else:
        pos[y][x] = n


for i in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for x in range(x1, x2+1):
        check(x, y1, i)
        check(x, y2, i)
    for y in range(y1+1, y2):
        check(x1, y, i)
        check(x2, y, i)

counter = Counter([find(parent, x) for x in parent])
answer = len(counter)-1

if pos[0][0] == -1:
    answer += 1

print(answer)
