import sys

N, M = map(int, input().split())

edge = [[sys.maxsize for _ in range(N+1)] for __ in range(N+1)]
dist = [sys.maxsize for _ in range(N+1)]
dist[1] = 0

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    edge[s][e] = min(edge[s][e], t)


def getDist():
    for j in range(1, N+1):
        if dist[j] == sys.maxsize:
            continue
        for k in range(1, N+1):
            if edge[j][k] == sys.maxsize:
                continue
            s, e, t = j, k, edge[j][k]

            dist[e] = min(dist[e], dist[s]+t)


for i in range(N-1):
    getDist()
tmp = dist.copy()

getDist()

for i in range(2, N+1):
    if dist[i] < tmp[i]:
        print(-1)
        sys.exit(0)

for i in range(2, N+1):
    if dist[i] == sys.maxsize:
        print(-1)
    else:
        print(dist[i])
