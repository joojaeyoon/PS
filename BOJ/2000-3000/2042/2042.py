import sys

N, M, K = map(int, input().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]

tmp = 1
while tmp < N:
    tmp *= 2
tmp *= 2

tree = [0 for _ in range(tmp+1)]


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start+end) >> 1

    tree[node] = init(start, mid, node*2)+init(mid+1, end, node*2+1)
    return tree[node]


def getSum(start, end, node, left, right):

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) >> 1

    return getSum(start, mid, node*2, left, right) + getSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, idx, diff):

    if idx < start or idx > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start+end) >> 1

    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2+1, idx, diff)


init(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(0, N-1, 1, b-1, c-arr[b-1])
        arr[b-1] = c
    else:
        print(getSum(0, N-1, 1, b-1, c-1))
