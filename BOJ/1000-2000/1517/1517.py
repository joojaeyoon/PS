N = int(input())

arr = list(map(int, input().split()))
tmp = [0 for _ in range(len(arr))]
cnt = 0


def merge(l, left, mid, right):
    global cnt
    i = left
    j = mid+1

    k = left

    while i <= mid and j <= right:
        if l[i] <= l[j]:
            tmp[k] = l[i]
            i += 1
        else:
            tmp[k] = l[j]
            j += 1
            cnt += mid-i+1
        k += 1

    for idx, limit in ((i, mid), (j, right)):
        while idx <= limit:
            tmp[k] = l[idx]
            idx += 1
            k += 1

    for i in range(left, right+1):
        l[i] = tmp[i]


def mergeSort(l, left, right):

    if left < right:
        mid = (left+right) >> 1
        mergeSort(l, left, mid)
        mergeSort(l, mid+1, right)
        merge(l, left, mid, right)


mergeSort(arr, 0, len(arr)-1)

print(cnt)
