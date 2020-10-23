import sys

N, Q = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

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


def update(start, end, node, idx, diff):

    if start <= idx and idx <= end:
        tree[node] += diff
    else:
        return

    if start == end:
        return

    mid = (start+end) >> 1

    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2+1, idx, diff)


def getSum(start, end, node, left, right):

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) >> 1

    return getSum(start, mid, node*2, left, right) + getSum(mid+1, end, node*2+1, left, right)


init(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x

    print(getSum(0, N-1, 1, x-1, y-1))
    update(0, N-1, 1, a-1, b-arr[a-1])
    arr[a-1] += b-arr[a-1]
