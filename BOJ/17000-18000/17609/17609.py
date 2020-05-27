
def checkPalindrome(s):
    left = 0
    right = len(s)-1

    while right > left:
        if s[left] != s[right]:
            if s[left+1:right+1] == s[left+1:right+1][::-1]:
                return 1
            elif s[left:right] == s[left:right][::-1]:
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 0


T = int(input())

strings = []

for _ in range(T):
    strings.append(input())

for s in strings:
    print(checkPalindrome(s))
