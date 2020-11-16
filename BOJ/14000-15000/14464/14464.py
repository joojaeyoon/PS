import sys

C, N = map(int, input().split())
chick = [int(sys.stdin.readline()) for _ in range(C)]
cow = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

chick.sort()
cow.sort(key=lambda x: (x[1], x[0]))
check = [True for _ in range(N)]
i, j = 0, 0

while i < N:
    a, b = cow[i]

    for k in range(j, len(chick)):
        if a <= chick[k] <= b:
            answer += 1
            del chick[k]
            break

    i += 1

print(answer)
