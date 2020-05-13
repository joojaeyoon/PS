import sys

N, M, V = map(int, input().split())
visited = [False for _ in range(N+1)]
children = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    children[a].append(b)
    children[b].append(a)

for c in children:
    c.sort()

visited[V] = True


def DFS(visited, num):

    print(num, end=" ")
    if sum(visited) == min(N, M+1):
        print()
        return

    for child in children[num]:
        if not visited[child]:
            visited[child] = True
            DFS(visited, child)


def BFS(visited, num):
    queue = []

    queue.append(num)

    while len(queue) != 0:
        num = queue[0]
        print(queue.pop(0), end=" ")
        for child in children[num]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
    print()


DFS(visited.copy(), V)
BFS(visited.copy(), V)
