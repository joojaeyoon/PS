A = int(input())
arr = list(map(int, input().split()))

dp1 = [1 for _ in range(A)]
dp2 = [1 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j] and dp1[j]+1 > dp1[i]:
            dp1[i] = dp1[j]+1

for i in range(A-1, -1, -1):
    for j in range(A-1, i, -1):
        if arr[i] > arr[j] and dp2[j]+1 > dp2[i]:
            dp2[i] = dp2[j]+1

ans = 0

for i in range(A):
    tmp = dp1[i]+dp2[i]-1
    ans = max(ans, tmp)

print(ans)
