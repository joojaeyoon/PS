# Programmers LV 2 카펫

def solution(brown, yellow):
    h=2
    result=brown+yellow

    while True:
        h+=1        
        w=h
        while w*h <= result and w >= h:
            if w*h == result and (h-2)*(w-2) >= yellow:
                return [w,h]
            w+=1

# solution(10,2)
# solution(8,1)
print(solution(24,24))

# brown + yellow = x * y
