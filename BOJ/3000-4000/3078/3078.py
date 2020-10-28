import sys
from collections import deque
N, K = map(int, input().split())
answer = 0
q = [deque([]) for _ in range(21)]

for i in range(N):
    length = len(sys.stdin.readline())-1

    while q[length] and i-q[length][0] > K:
        q[length].popleft()

    answer += len(q[length])

    q[length].append(i)

print(answer)
