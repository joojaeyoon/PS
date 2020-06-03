T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    div = N//4

    arr = list(input())*2
    nums = set()

    for j in range(len(arr)//2):
        tmp = "".join(arr[j:j+div])
        nums.add(int(tmp, 16))

    print(f"#{i+1}", sorted(list(nums), reverse=True)[K-1])
