# Programmers LV 3 섬 연결하기

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

def find(parent,x):
    if parent[x]==x: 
        return x
    else:
        x=find(parent,parent[x])
        return x

def check(parent,a,b):
    if find(parent,a) == find(parent,b):
        return 1
    return 0

def solution(n, costs):
    answer = 0

    parent=[i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])

    for i in range(len(costs)):
        a,b,c=costs[i]
        if not check(parent,a,b):    
            union(parent,a,b)
            answer+=c        
        
    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])