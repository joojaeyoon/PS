import sys

K, N = map(int, input().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]

lo, hi = 1, max(lan)

while lo <= hi:
    mid = (lo+hi)//2

    lines = 0
    for i in lan:
        lines += i // mid

    if lines >= N:
        lo = mid+1
    else:
        hi = mid-1
print(hi)
