N = int(input())

towers = list(map(int, input().split()))
answer = [0 for _ in range(N)]

stack = [(0, towers[0])]
for i in range(1, N):
    while stack and stack[-1][1] < towers[i]:
        answer[i] = 0
        stack.pop()

    if stack and stack[-1][1] >= towers[i]:
        answer[i] = stack[-1][0]+1

    stack.append((i, towers[i]))

print(*answer)
