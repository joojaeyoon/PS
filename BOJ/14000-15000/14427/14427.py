import sys
import math

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())

tmp = int(math.log(N, 2))+2
tree = [0 for _ in range(2**tmp+1)]


def init(start, end, node):

    if start == end:
        tree[node] = [start, arr[start]]
        return tree[node]

    mid = (start+end) >> 1

    left = init(start, mid, node*2)
    right = init(mid+1, end, node*2+1)

    tree[node] = sorted([left, right], key=lambda x: (x[1], x[0]))[0]

    return tree[node]


def update(start, end, node, idx):
    if not (start <= idx and idx <= end):
        return tree[node]

    if start == end:
        tree[node] = [idx, arr[idx]]
        return tree[node]

    mid = (start+end) >> 1
    left = update(start, mid, node*2, idx)
    right = update(mid+1, end, node*2+1, idx)

    tree[node] = sorted([left, right], key=lambda x: (x[1], x[0]))[0]

    return tree[node]


init(0, N-1, 1)

for _ in range(M):
    data = sys.stdin.readline().split()

    if len(data) == 1:
        print(tree[1][0]+1)
    else:
        _, idx, val = map(int, data)
        arr[idx-1] += val-arr[idx-1]
        update(0, N-1, 1, idx-1)
