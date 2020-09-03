def solution(brown, yellow):
    height=2
    result=brown+yellow

    while True:
        height+=1        
        width=height
        while width*height <= result and width >= height:
            if width*height == result and (height-2)*(width-2) >= yellow:
                return [width,height]
            width+=1
            
# solution(10,2)
# solution(8,1)
print(solution(24,24))

# brown + yellow = x * y