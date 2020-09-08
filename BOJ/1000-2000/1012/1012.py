import sys
from collections import deque

T=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for _ in range(T):
    M,N,K=map(int,input().split())
    MAP=[[0 for __ in range(M)] for ___ in range(N)]
    visited=[[False for __ in range(M)] for ___ in range(N)]
    pos=[]
    cnt=0

    for i in range(K):
        x,y=map(int,sys.stdin.readline().split())
        pos.append([x,y])
        MAP[y][x]=1
    
    
    q=deque()

    for i,p in enumerate(pos):
        if not visited[pos[i][1]][pos[i][0]]:
            q.append(pos[i])
            cnt+=1
              
            while len(q)!=0:
                x,y=q.popleft()

                for j in range(4):
                    nx=x+dx[j]
                    ny=y+dy[j]

                    if 0 <= nx and nx < M and 0 <= ny and ny < N \
                        and not visited[ny][nx] and MAP[ny][nx]==1:
                        visited[ny][nx]=True
                        q.append([nx,ny])
                        
                        
    print(cnt)            


        
    