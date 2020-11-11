N = int(input())
weight = sorted(list(map(int, input().split())))

s = 1

for i in range(N):
    if s < weight[i]:
        break
    s += weight[i]

print(s)
