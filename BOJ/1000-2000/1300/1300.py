N=int(input())
k=int(input())

lo=1
hi=k
answer=-1

while lo<=hi:
    mid=(lo+hi)>>1
    cnt=0

    for i in range(1,N+1):
        cnt+=min(int(mid/i),N)

    if cnt < k:
        lo=mid+1
    else:
        answer=mid
        hi=mid-1

print(answer)