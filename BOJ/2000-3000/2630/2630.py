import sys

N=int(input())

MAP=[]

white=0
blue=0

def check(x,y,size):
    cnt=0

    for i in range(size):
        for j in range(size):
            if MAP[i+y][j+x]==1:
                cnt+=1

    if cnt==size**2:
        global blue
        blue+=1
        return 1
    elif cnt==0:
        global white
        white+=1
        return 2
    else:
        return 3

def divide(paper,x,y,size):

    pos=[[x,y],
        [x,y+size//2],
        [x+size//2,y],
        [x+size//2,y+size//2]]

    for i in range(4):
        x,y=pos[i]
        result=check(x,y,size//2)
        if result==3:
            divide(paper,x,y,size//2)

for _ in range(N):
    MAP.append(list(map(int,sys.stdin.readline().split())))

divide(MAP,0,0,N)

print(white)
print(blue)