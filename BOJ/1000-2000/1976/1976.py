# 1976 여행가자

import sys


def getParent(parent,x):
    if parent[x]==x: return x
    parent[x] = getParent(parent,parent[x])

    return parent[x]

def unionParent(parent,a,b):
    a=getParent(parent,a)
    b=getParent(parent,b)
    if a<b: parent[b]=a
    else: parent[a]=b

N=int(input())
M=int(input())

edge=[[] for _ in range(N+1)]
parent=[i for i in range(N+1)]
answer="YES"

for i in range(1,N+1):
    edge[i]=[0]+list(map(int,sys.stdin.readline().split()))

trip=list(map(int,sys.stdin.readline().split()))


for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j or edge[i][j]==0:
            continue
        unionParent(parent,i,j)
tmp=parent[trip[0]]

for t in trip[1:]:
    if tmp != parent[t]:
        answer="NO"
        break
        
print(answer)