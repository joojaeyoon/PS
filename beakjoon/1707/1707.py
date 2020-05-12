import sys

sys.setrecursionlimit(10**8)

K = int(input())


def dfs(color, graph, num, c):

    color[num] = c

    for i in graph[num]:
        if not color[i]:
            dfs(color, graph, i, 3-c)


def isBipartiteGraph(color, graph):

    for i in range(len(graph)):
        for j in graph[i]:
            if color[i] == color[j]:
                return False

    return True


for _ in range(K):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    color = [0 for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if not color[i]:
            dfs(color, graph, i, 1)

    if isBipartiteGraph(color, graph):
        print("YES")
    else:
        print("NO")
