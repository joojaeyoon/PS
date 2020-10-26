import sys
import bisect as b

N = int(input())
arr = list(map(int, input().split()))
lis = [-sys.maxsize]


for i in range(N):
    if arr[i] >= lis[-1]:
        lis.append(arr[i])
    else:
        idx = b.bisect_left(lis, arr[i])
        lis[idx] = arr[i]


print(N-len(lis)+1)
