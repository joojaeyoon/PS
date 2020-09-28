import sys
import heapq

V,E=map(int,input().split())
K=int(input())

edge=[[] for __ in range(V+1)]
costs=[3*10**6 for _ in range(V+1)]
costs[K]=0

for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())

    edge[u].append((v,w))

hq=[]

heapq.heappush(hq,[0,K])

while hq:
    dist,cur=heapq.heappop(hq)

    if costs[cur] < dist:
        continue
    
    for i in range(len(edge[cur])):
        nxt=edge[cur][i][0]
        nextDist=edge[cur][i][1] + dist

        if nextDist < costs[nxt]:
            costs[nxt]=nextDist
            heapq.heappush(hq,[nextDist,nxt])

for c in costs[1:]:
    if c!=3*10**6:
        print(c)
    else:
        print("INF")
