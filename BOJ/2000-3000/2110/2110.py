import sys

N,C=map(int,sys.stdin.readline().split())
dists=[]

for _ in range(N):
    dists.append(int(sys.stdin.readline()))

dists.sort()

lo=0
hi=dists[-1]
answer=0

while lo <= hi:
    mid=(lo+hi)>>1
    c_cnt=C-1
    cnt=0
    pos=[0]

    for i in range(1,N):
        d=dists[i]-dists[pos[-1]]
        if d >= mid and c_cnt>0:
            c_cnt-=1
            pos.append(i)
            cnt+=1
    
    if cnt >= (C-1):
        lo=mid+1
        answer=max(answer,mid)
    else:
        hi=mid-1

print(answer)