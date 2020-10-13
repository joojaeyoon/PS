
N = int(input())
times = [0]
answer = 0

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    times.append(tmp[0])
    mx = 0
    for t in tmp[2:]:
        mx = max(mx, times[t])
    times[i] += mx
    if answer < times[i]:
        answer = times[i]

print(answer)
