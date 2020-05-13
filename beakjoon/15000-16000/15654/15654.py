N, M = map(int, input().split())

visited = [False for i in range(N)]

nums = sorted(list(map(int, input().split())))


def print_set(arr, selected, toPick):

    if toPick == 0:
        print(*selected)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            print_set(arr, selected+[arr[i]],  toPick-1)
            visited[i] = False


print_set(nums, [], M)
