def solution(inputString):
    answer = 0
    stack = []
    bracket = "(){}[]<>"

    for s in inputString:
        if s in bracket:
            if s in bracket[::2]:
                stack.append(s)
            elif bracket[bracket.index(s)-1] in stack:
                stack.remove(bracket[bracket.index(s)-1])
                answer += 1
            else:
                return -1

    return answer


inputs = ["Hello,world!", "line [plus]",
          "if (Count of eggs is 4.) {Buy milk.}", ">_<"]
outputs = [0, 1, 2, -1]


for i in range(len(inputs)):
    output = solution(inputs[i])

    if output == outputs[i]:
        print("정답")
    else:
        print("땡")
