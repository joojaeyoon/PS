N,M,L=map(int,input().split())

pos=[0]+sorted(list(map(int,input().split())))+[L]

answer=1000
lo=0
hi=L

while lo <= hi:
    mid=(lo+hi)>>1
    cnt=0

    for i in range(1,len(pos)):
        cnt+=int((pos[i]-pos[i-1]-1)/mid)
    
    if cnt > M:
        lo=mid+1
    else:
        answer=min(answer,mid)
        hi=mid-1

print(answer)