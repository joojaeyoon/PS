
def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))[1:]
    total = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            total += gcd(nums[i], nums[j])

    print(total)
