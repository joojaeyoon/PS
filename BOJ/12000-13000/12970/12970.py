N, K = map(int, input().split())
answer = ""
arr = [0 for _ in range(N)]
tmp = K

for i in range(int(N/2), 0, -1):
    if tmp >= i:

        arr[i] = int(tmp/i)
        tmp %= i

for i in range(int(N/2), 0, -1):
    answer += arr[i]*"A"
    answer += "B"

if len(answer) > N:
    print(-1)
    exit(0)

answer = "B"*(N-len(answer))+answer

print(answer)
