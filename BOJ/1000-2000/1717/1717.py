import sys

def getParent(parent,x):
    if parent[x] == x: return x
    else:
        parent[x]=getParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a=getParent(parent,a)
    b=getParent(parent,b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

N,M=map(int,input().split())
parent=[i for i in range(N+1)]

for _ in range(M):
    cmd,a,b=map(int,sys.stdin.readline().split())
    
    if cmd==0:
        unionParent(parent,a,b)
    else:
        a=getParent(parent,a)
        b=getParent(parent,b)
        if a==b: print("YES")
        else: print("NO")