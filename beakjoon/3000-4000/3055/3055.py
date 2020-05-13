from collections import deque

R, C = map(int, input().split())

visited = [[-1 for _ in range(C)] for __ in range(R)]
m = [[] for _ in range(R)]

Q = deque()

D = []
S = []
water = []

for i in range(R):
    tmp = input()
    for j in range(C):
        if tmp[j] == "D":
            D = [j, i]
        elif tmp[j] == "*":
            water.append([j, i])
        elif tmp[j] == "S":
            S = [j, i]

        m[i].append(tmp[j])

for w in water:
    Q.append(w)

Q.append(S)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited[S[1]][S[0]] = 0

while len(Q) != 0:
    x, y = Q.popleft()

    if x == D[0] and y == D[1]:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx and nx < C and 0 <= ny and ny < R:
            if m[y][x] == "*":
                if m[ny][nx] == "." and visited[ny][nx] == -1:
                    m[ny][nx] = "*"
                    Q.append([nx, ny])
            elif (m[ny][nx] == "." or m[ny][nx] == "D") and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x]+1
                Q.append([nx, ny])

if visited[D[1]][D[0]] == -1:
    print("KAKTUS")
else:
    print(visited[D[1]][D[0]])
