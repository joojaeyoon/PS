
def sieve():
    nums = [True for i in range(123456*2+1)]

    for i in range(2, len(nums)):
        if nums[i] == True:
            for j in range(i+i, len(nums), i):
                nums[j] = False

    return nums


nums = sieve()

while True:
    num = int(input())

    if num == 0:
        break

    new_nums = nums[num+1:2*num+1]

    count = new_nums.count(True)
    print(count)
