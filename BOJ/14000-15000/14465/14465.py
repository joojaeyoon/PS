import sys

N, K, B = map(int, input().split())
check = [True for _ in range(N+1)]
answer = K

for _ in range(B):
    idx = int(sys.stdin.readline())
    check[idx] = False

cnt = check[1:K+1].count(False)
answer = cnt
i = 2
while i <= N-K+1:
    if not check[i-1]:
        cnt -= 1
    if not check[i+K-1]:
        cnt += 1
    answer = min(answer, cnt)
    i += 1

print(answer)
