import sys

def getParent(parent,x):
    if parent[x]==x: return x
    else:
        parent[x]=getParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a=getParent(parent,a)
    b=getParent(parent,b)

    total=counter[a]+counter[b]

    if a < b: 
        parent[b]=a
        counter[b]=total
        counter[a]=counter[b]
    elif a > b: 
        parent[a]=b
        counter[a]=total
        counter[b]=counter[a]

T=int(input())

for _ in range(T):
    F=int(input())
    parent={}
    counter={}

    for i in range(F):
        a,b=sys.stdin.readline().split()
        cnt=0
        if not parent.get(a,False):
            parent[a]=a
            counter[a]=1
        if not parent.get(b,False):
            parent[b]=b
            counter[b]=1
        
        unionParent(parent,a,b)
        print(counter[parent[a]])