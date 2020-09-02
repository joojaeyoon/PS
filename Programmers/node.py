from collections import deque

def solution(n, edge):
    answer = 0
    rel=[[] for i in range(n+1)]
    visited=[False for i in range(n+1)]
    costs=[50001 for i in range(n+1)]

    for e in edge:
        rel[e[0]].append(e[1])
        rel[e[1]].append(e[0])

    visited[1]=True

    q=deque()
    q.append([1,0])
    costs[0]=-1

    while len(q)!=0:
        node,dist=q.popleft()

        costs[node]=min(costs[node],dist)
        
        for r in rel[node]:
            if not visited[r]:
                q.append([r,dist+1])
                visited[r]=True
    val=1

    for i in range(1,n+1):
        if costs[i]==val:
            answer+=1
        elif costs[i] > val:
            val=costs[i]
            answer=1

    return answer

result=solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(result)
