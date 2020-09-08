import sys
from collections import deque

C=int(input())
P=int(input())

rel=[[] for _ in range(C+1)]
visited=[False for _ in range(C+1)]

cnt=0

for _ in range(P):
    a,b=map(int,sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)

q=deque()
q.append(1)
visited[1]=True

while len(q)!=0:
    num=q.popleft()

    for r in rel[num]:
        if not visited[r]:
            q.append(r)
            visited[r]=True
            cnt+=1

print(cnt)