# Programmers LV 4 지형 이동

from collections import deque

def getParent(parent,x):
    if parent[x]==x: return x
    else:
        return getParent(parent,parent[x])

def union(parent,a,b):

    a=getParent(parent,a)
    b=getParent(parent,b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

def solution(land, height):
    answer = 0

    N=len(land)

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    area=[[-1 for __ in range(N)] for _ in range(N)]
    min_diff=set()

    q=deque()
    counter=-1

    for i in range(N):
        for j in range(N):
            if area[i][j]!=-1:
                continue
            q.append([j,i])
            counter+=1
            while q:
                x,y=q.popleft()
                area[y][x]=counter

                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    if 0 <= nx and nx < N and \
                        0 <= ny and ny < N and \
                        area[y][x] != area[ny][nx] and \
                        abs(land[y][x]-land[ny][nx]) <= height:
                            area[ny][nx]=counter
                            q.append([nx,ny])
    for y in range(N):
        for x in range(N):

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0 <= nx and nx < N and \
                    0 <= ny and ny < N and \
                    area[y][x] != area[ny][nx]:
                    a=min(area[y][x],area[ny][nx])
                    b=max(area[y][x],area[ny][nx])
                    d=abs(land[y][x]-land[ny][nx])
                    min_diff.add((a,b,d))
            
    
    min_diff=sorted(list(min_diff),key=lambda x: x[2])

    parent=[i for i in range(counter+1)]

    for m in min_diff:
        a,b,cost=m
        if getParent(parent,a)!=getParent(parent,b):
            union(parent,a,b)
            answer+=cost
    return answer

solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)