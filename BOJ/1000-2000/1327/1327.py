from collections import deque


N, K = map(int, input().split())

arr = "".join(input().split())

target = "".join(sorted(arr))

q = deque()

q.append([arr, 0])

count = -1

visited = {}

while len(q) != 0:
    A, C = q.popleft()

    if A == target:
        count = C
        break

    if visited.get(A, True):
        visited[A] = False
        for i in range(N-K + 1):
            q.append([A[:i]+A[i:i+K][::-1]+A[i+K:], C+1])

print(count)
