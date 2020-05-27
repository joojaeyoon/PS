from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(100001)]


def bfs(n, k):
    global visited
    q = deque()

    q.append([n, 0])

    while len(q) != 0:

        pos, t = q.popleft()
        visited[pos] = True

        if pos == k:
            print(t)
            break

        new_pos = [pos+1, pos*2, pos-1]

        for p in new_pos:
            if 0 <= p and p <= 100000 and not visited[p]:
                q.append([p, t+1])


if N >= K:
    print(N-K)
else:
    bfs(N, K)
