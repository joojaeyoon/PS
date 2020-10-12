infix = input()
postfix = ""

stack = []

op = {"+": 1, "-": 1, "*": 2, "/": 2}

for c in infix:
    if c.isalpha():
        postfix += c
    elif c == ")":
        while stack[-1] != "(":
            postfix += stack.pop()
        stack.pop()
    else:
        if c != "(":
            while stack and stack[-1] != "(" and op[stack[-1]] >= op[c]:
                postfix += stack.pop()
        stack.append(c)

while stack:
    postfix += stack.pop()

print(postfix)
