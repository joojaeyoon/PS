import sys
import heapq

N=int(input())
M=int(input())

edge=[[10**5 for __ in range(N+1)]for _ in range(N+1)]

for _ in range(M):
    u,v,w=map(int,sys.stdin.readline().split())

    edge[u][v]=min(edge[u][v],w)
start,end=map(int,sys.stdin.readline().split())

costs=[10**11 for _ in range(N+1)]
costs[start]=0

hq=[[0,start]]

while hq:
    cost,cur=heapq.heappop(hq)

    if costs[cur] < cost:
        continue

    for i in range(1,N+1):
        if edge[cur][i]!=10**5:
            nxt=i
            nextDist=edge[cur][i]+cost
            
            if nextDist < costs[nxt]:
                heapq.heappush(hq,[nextDist,i])
                costs[nxt]=nextDist

print(costs[end])