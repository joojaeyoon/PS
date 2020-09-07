
counter={}

N=int(input())
arr=list(map(int,input().split()))

M=int(input())
arr2=list(map(int,input().split()))


for i in range(N):
    if not counter.get(arr[i],False):
        counter[arr[i]]=0
    counter[arr[i]]+=1

for i in range(M):
    if not counter.get(arr2[i],False):
        counter[arr2[i]]=0
    print(counter[arr2[i]],end=" ")