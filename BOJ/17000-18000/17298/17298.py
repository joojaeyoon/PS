N = int(input())
arr = list(map(int, input().split()))

stack = [(0, arr[0])]
answer = [-1 for _ in range(N)]


for i in range(1, len(arr)):
    while stack and stack[-1][1] < arr[i]:
        answer[stack[-1][0]] = arr[i]
        stack.pop()

    stack.append((i, arr[i]))

print(*answer)
