N = int(input())

nums = list(map(int, input().split()))

op_count = list(map(int, input().split()))

op_func = [
    lambda a, b: a+b,
    lambda a, b: a-b,
    lambda a, b: a*b,
    lambda a, b: int(a/b)
]

answer = [-1000000001, 1000000001]


def select(toPick, length, N):
    global answer
    if toPick == 0:
        answer[0] = max(answer[0], N)
        answer[1] = min(answer[1], N)
        return

    for i in range(4):
        if op_count[i] != 0:
            op_count[i] -= 1
            select(toPick-1, length,
                   op_func[i](N, nums[length-toPick+1]))
            op_count[i] += 1


select(len(nums)-1, len(nums)-1, nums[0])

print(answer[0])
print(answer[1])
