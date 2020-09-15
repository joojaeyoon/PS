# Programmers LV 3 방문 길이

def solution(dirs):
    D={"U":[0,-1],"L":[-1,0],"D":[0,1],"R":[1,0]}
    x,y=5,5

    counter={}
    for d in dirs:
        nx,ny=D[d]
        nx+=x
        ny+=y

        if 0 <= nx and nx < 11 and\
            0 <= ny and ny <11:
            tmp=sorted([[x,y],[nx,ny]],key=lambda x: (x[0],x[1]))
            c=str(tmp[0][0])+str(tmp[0][1])+str(tmp[1][0])+str(tmp[1][1])
            counter[c]=1
            x=nx
            y=ny
            
    return len(counter)

solution("ULURRDLLU")