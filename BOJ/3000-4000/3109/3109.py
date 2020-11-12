import sys

R, C = map(int, input().split())
MAP = [list(sys.stdin.readline()[:-1]) for _ in range(R)]
answer = 0

pos = [(y, 0) for y in range(R)]


def dfs(x, y):
    if y < 0 or y >= R:
        return 0
    if MAP[y][x] == 'x':
        return 0

    MAP[y][x] = 'x'
    if x == C-1:
        return 1

    if dfs(x+1, y-1):
        return
    if dfs(x+1, y):
        return 1
    if dfs(x+1, y+1):
        return 1

    return 0


for y, x in pos:
    answer += dfs(x, y)
print(answer)
