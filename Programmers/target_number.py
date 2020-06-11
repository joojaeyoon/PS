from collections import deque


def solution(numbers, target):
    answer = 0

    q = deque()
    q.append("")

    while len(q) != 0:

        op = q.popleft()

        if len(op) == len(numbers):
            result = 0
            for i in range(len(op)):
                if op[i] == "+":
                    result += numbers[i]
                else:
                    result -= numbers[i]
            if result == target:
                answer += 1
            continue

        q.append(op+"+")
        q.append(op+"-")

    return answer


print(solution([1, 1, 1, 1, 1], 3))
