N, K = map(int, input().split())
num = input()

stack = [num[0]]

for i in range(1, N):
    while K != 0 and stack and stack[-1] < num[i]:
        stack.pop()
        K -= 1

    if K == 0:
        for j in range(i, N):
            stack.append(num[j])
        break

    stack.append(num[i])

for _ in range(K):
    stack.pop()

print("".join(stack))
