import sys

N=int(input())
answer=0
platforms=[]

for _ in range(N):
    y,x,x2=map(int,sys.stdin.readline().split())
    platforms.append([y,x,x2-1])

platforms.sort(key=lambda x: x[0],reverse=True)

for i in range(N):
    y,x,x2=platforms[i]
    
    left,right=False,False

    for j in range(i+1,N):
        if left and right:
            break
        ny,nx,nx2=platforms[j]

        if not left and nx <= x and x <= nx2:
            left=True
            answer+=y-ny                    
        if not right and nx <= x2 and x2 <= nx2:
            right=True
            answer+=y-ny
    if not left:
        answer+=y
    if not right:
        answer+=y

print(answer)
        

