from bisect import bisect_left

N=int(input())
arr=list(map(int,input().split()))

ans=[]

for x in arr:
    if not ans or x > ans[-1]:
        ans.append(x)
    else:
        ans[bisect_left(ans,x)]=x

print(len(ans))