import sys

N = int(input())
arr = [(i, int(sys.stdin.readline())) for i in range(N)]
arr2 = sorted(arr, key=lambda x: x[1])

answer = 0
for i in range(N):
    answer = max(answer, arr2[i][0]-i)

print(answer+1)
