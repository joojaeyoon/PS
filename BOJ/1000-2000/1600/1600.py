import sys
from collections import deque

K=int(input())

W,H=map(int,input().split())
visited=[[[False for ___ in range(31)] for _ in range(W)]for __ in range(H)]
visited[0][0][K]=0

answer=10**5

MAP=[]

for _ in range(H):
    MAP.append(list(map(int,sys.stdin.readline().split())))

q=deque()

q.append([0,0,K,0])

dx=[1,-1,0,0]
dy=[0,0,1,-1]

kx=[-2,-1,1,2,-2,-1,1,2]
ky=[-1,-2,-2,-1,1,2,2,1]

while q:
    x,y,k,cost=q.popleft()

    if x==W-1 and y==H-1:
        answer=min(answer,cost)
        continue

    if k > 0:
        for i in range(8):
            nx=x+kx[i]
            ny=y+ky[i]

            if 0 <= nx and nx < W and 0 <= ny and ny < H and\
                not visited[ny][nx][k-1] and MAP[ny][nx] != 1:
                visited[ny][nx][k-1] = True
                q.append([nx, ny, k - 1, cost + 1])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < W and 0 <= ny and ny < H and \
            not visited[ny][nx][k] and MAP[ny][nx] != 1:
            visited[ny][nx][k] = True
            q.append([nx, ny, k, cost + 1])

if answer==10**5:
    print(-1)
else:
    print(answer)