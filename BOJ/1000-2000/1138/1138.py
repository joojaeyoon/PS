N = int(input())
count = list(map(int, input().split()))

answer = [N]

for i in range(N-2, -1, -1):
    answer.insert(count[i], i+1)

print(*answer)
