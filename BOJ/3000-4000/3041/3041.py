puzzle = ""

answer = 0

for _ in range(4):
    puzzle += input()

for i, p in enumerate(puzzle):
    C = chr(i+ord("A"))
    if C != p and p != ".":
        cx = (ord(C)-ord("A")) % 4
        cy = int((ord(C)-ord("A")) / 4)

        px = (ord(p)-ord("A")) % 4
        py = int((ord(p)-ord("A"))/4)

        answer += abs(cx-px)+abs(cy-py)


print(answer)
