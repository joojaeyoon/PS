
def getData(m, h):
    max_height = 0

    for i in range(N):
        m.append(list(map(int, input().split())))
        for j in range(N):
            if m[i][j] > max_height:
                max_height = m[i][j]
                h.clear()
                h.append([i, j])
            elif m[i][j] == max_height:
                h.append([i, j])


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_length = 0


def dfs(m, length, used, K, pos):
    n = len(m)
    flag = True

    x, y = pos

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n and m[nx][ny] != -1:
            if m[nx][ny] < m[x][y]:
                tmp = m[x][y]
                m[x][y] = -1
                dfs(m, length+1, used, K, [nx, ny])
                m[x][y] = tmp

                flag = False
            else:
                if not used and K >= m[nx][ny]-m[x][y]+1:
                    tmp = m[nx][ny]
                    tmp2 = m[x][y]

                    m[nx][ny] = m[x][y]-1
                    m[x][y] = -1
                    used = True

                    dfs(m, length+1, used, K, [nx, ny])

                    used = False
                    m[nx][ny] = tmp
                    m[x][y] = tmp2

                    flag = False
    if flag:
        global max_length
        max_length = max(max_length, length)
        return


T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    q = []
    m = []

    getData(m, q)

    for p in q:
        dfs(m, 1, False, K, p)

    print(f"#{i+1} {max_length}")

    max_length = 0
