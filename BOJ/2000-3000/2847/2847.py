N = int(input())
level = [int(input()) for _ in range(N)]
answer = 0

for i in reversed(range(1, N)):
    if level[i] <= level[i-1]:
        tmp = level[i-1]-level[i]+1
        answer += tmp
        level[i-1] -= tmp

print(answer)
