import sys
from collections import deque


def solution(N, number):
    answer = sys.maxsize

    q = deque()
    q.append([0, 0])

    while len(q) != 0:

        num, count = q.popleft()

        if count > 8:
            continue

        if num == number:
            answer = min(answer, count)

        q.append([num+N, count+1])
        q.append([num-N, count+1])
        q.append([num//N, count+1])
        q.append([num*N, count+1])
        q.append([num+1, count+2])
        q.append([num-1, count+2])
        q.append([num-(N*10+N), count+2])
        q.append([num+(N*10+N), count+2])
        q.append([num//(N*10+N), count+2])
        q.append([num*(N*10+N), count+2])

    return answer if answer <= 8 else -1


print(solution(5, 12))

print(solution(2, 11))
