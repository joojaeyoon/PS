import sys
from collections import deque

read = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0 for _ in range(N+1)] for __ in range(N+1)]

for _ in range(K):
    y, x = map(int, read().split())
    board[y][x] = 2

L = int(input())
moves = [list(read().split()) for _ in range(L)]

q = deque([[1, 1]])

time = 1

mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]

idx = 0
for i in range(L):
    while time <= int(moves[i][0]):
        hy, hx = q[0]

        nx = hx+mx[idx]
        ny = hy+my[idx]

        if not (0 < nx <= N and 0 < ny <= N) or \
                board[ny][nx] == 1:
            print(time)
            exit(0)

        q.appendleft([ny, nx])
        if board[ny][nx] == 0:
            ty, tx = q[-1]
            board[ty][tx] = 0
            q.pop()
        board[ny][nx] = 1

        time += 1
    if moves[i][1] == "D":
        idx = (idx+1) % 4
    else:
        idx = (idx-1) % 4

y, x = q.popleft()

x += mx[idx]
y += my[idx]
time += 1
while (0 < x <= N and 0 < y <= N) and board[y][x] != 1:
    x += mx[idx]
    y += my[idx]
    time += 1

print(time-1)
