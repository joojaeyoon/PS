import sys

T = int(input())

for __ in range(T):
    N, M = map(int, input().split())
    student = []
    connection = [-1 for _ in range(N+1)]
    answer = 0

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        student.append((a, b))

    student.sort(key=lambda x: x[1])

    for i, stu in enumerate(student):
        for j in range(stu[0], stu[1]+1):
            if connection[j] == -1:
                answer += 1
                connection[j] = i
                break

    print(answer)
