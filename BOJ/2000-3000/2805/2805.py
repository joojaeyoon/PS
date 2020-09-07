import sys
from collections import Counter

N,M=map(int,sys.stdin.readline().split())

trees=Counter(list(map(int,sys.stdin.readline().split())))

lo=0
hi=max(trees)

answer=0

while lo <= hi :
    mid=(lo+hi)>>1
    total=0

    for height,number in trees.items():
        if height > mid:
            total+=(height-mid)*number

    if total >= M :
        lo=mid+1
        if answer < mid:
            answer=mid
    else:
        hi=mid-1

print(answer)