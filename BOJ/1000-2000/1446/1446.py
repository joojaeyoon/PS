N,D=map(int,input().split())

short=[]
dist=[i for i in range(D+1)]

for _ in range(N):
    tmp=list(map(int,input().split()))
    if tmp[1] <= D:
        short.append(tmp)

short.sort(key=lambda x: x[0])

idx=0
for i in range(D+1):
    if i!=0:
        dist[i]=min(dist[i],dist[i-1]+1)
    while idx < len(short) and short[idx][0]==i:
        start,end,cost=short[idx]
        dist[end]=min(dist[end],dist[start]+cost)
        idx+=1

print(dist[-1])
