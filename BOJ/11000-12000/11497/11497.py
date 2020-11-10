T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0 for _ in range(N)]

    arr.sort()
    idx = 0
    for i in range(0, N, 2):
        new_arr[idx] = arr[i]
        idx += 1
    idx = -1
    for i in range(1, N, 2):
        new_arr[idx] = arr[i]
        idx -= 1

    answer = abs(new_arr[0]-new_arr[-1])

    for i in range(N-1):
        answer = max(answer, abs(new_arr[i]-new_arr[i+1]))

    print(answer)
