# Programmers LV 2 큰 수 만들기

def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=lambda x: x*3)

    return str(int("".join(numbers[::-1])))


print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))
