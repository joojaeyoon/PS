for i in range(10):
    l = int(input())
    arr = list(input())
    stack = []

    flag = True

    for j in range(l):
        if arr[j] in ("{", "[", "(", "<"):
            stack.append(arr[j])
        else:
            if abs(ord(stack[-1])-ord(arr[j])) > 2:
                flag = False
                break
            else:
                stack.pop()

    print(f"#{i+1} {int(flag)}")
