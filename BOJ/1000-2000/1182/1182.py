
N, S = list(map(int, input().split()))

nums = list(map(int, input().split()))

count = 0


def dfs(idx, total, size):
    global count

    if idx == N:
        if total == S and size != 0:
            count += 1
        return

    dfs(idx+1, total+nums[idx], size+1)
    dfs(idx+1, total, size)


dfs(0, 0, 0)

print(count)
