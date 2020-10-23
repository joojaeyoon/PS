import sys

N, M = map(int, input().split())

arr = [0]+[int(sys.stdin.readline()) for _ in range(N)]
tmp = 1
while tmp < N:
    tmp *= 2
tmp *= 2
tree = [0 for _ in range(tmp+1)]


def init(start, end, node):

    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]

    mid = (start+end) >> 1

    left = init(start, mid, node*2)
    right = init(mid+1, end, node*2+1)

    tree[node] = (max(left[0], right[0]), min(left[1], right[1]))
    return tree[node]


def find(start, end, node, left, right):

    if left > end or right < start:
        return (-sys.maxsize, sys.maxsize)

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) >> 1

    l = find(start, mid, node*2, left, right)
    r = find(mid+1, end, node*2+1, left, right)

    return (max(l[0], r[0]), min(l[1], r[1]))


init(1, N, 1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    print(*find(1, N, 1, a, b)[::-1])
