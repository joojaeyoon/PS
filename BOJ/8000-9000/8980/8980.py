import sys

N, C = map(int, input().split())
M = int(input())
capacity = [C for _ in range(N+1)]
answer = 0

info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
info.sort(key=lambda x: (x[1], x[0]))

for s, e, cost in info:
    tmp = cost

    for i in range(s, e):
        tmp = min(tmp, capacity[i])

    for i in range(s, e):
        capacity[i] -= tmp
    answer += tmp
print(answer)
