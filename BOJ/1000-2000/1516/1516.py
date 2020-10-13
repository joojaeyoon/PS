from collections import deque

N = int(input())
times = [0]
edge = [[]for _ in range(N+1)]
pre_build_cnt = [0 for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))[:-1]
    times.append(tmp[0])
    pre_build_cnt[i] += len(tmp)-1
    for b in tmp[1:]:
        edge[b].append(i)

results = [0 for _ in range(N+1)]
q = deque()

for i in range(1, N+1):
    if pre_build_cnt[i] == 0:
        results[i] = times[i]
        q.append((i, 0))

for _ in range(N):
    x, cnt = q.popleft()

    for e in edge[x]:
        pre_build_cnt[e] -= 1
        results[e] = max(results[e], results[x]+times[e])
        if pre_build_cnt[e] == 0:
            q.append((e, cnt+1))

for r in results[1:]:
    print(r)
