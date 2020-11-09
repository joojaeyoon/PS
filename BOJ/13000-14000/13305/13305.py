N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

answer = 0

i = 0
while i < N-1:

    j = i+1

    while j < N-1:
        if gas[j] < gas[i]:
            break
        j += 1

    for d in range(i, j):
        answer += gas[i]*dist[d]
    i = j

print(answer)
