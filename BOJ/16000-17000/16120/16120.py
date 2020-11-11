S = input()

stack = []

ppap = list("PPAP")

for c in S:
    stack.append(c)

    if len(stack) >= 4:
        if stack[-4:] == ppap:
            for i in range(4):
                stack.pop()
            stack.append("P")
if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")
