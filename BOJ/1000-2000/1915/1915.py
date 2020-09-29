import sys

N,M=map(int,input().split())
arr=[]
answer=0

for _ in range(N):
    arr.append(list(map(int,list(sys.stdin.readline()[:-1]))))

for i in range(1,N):
    for j in range(1,M):
        if arr[i][j]!=0:
            arr[i][j]=min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1])+1

for a in arr:
    answer=max(answer,max(a))

print(answer**2)