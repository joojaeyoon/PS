# Programmers LV 4 KAKAO 추석 트래픽

def to_second(time):
    time=time.split()
    t=float(time[2][:-1])
    time=time[1].split(":")
    second=int(time[0])*3600
    second+=int(time[1])*60
    second+=float(time[2])

    start=second-t+0.001
    end=second
    
    return [start,end]

def solution(lines):
    answer = 0
    N=len(lines)

    for i in range(N):
        lines[i]=to_second(lines[i])
    for i in range(N):
        for k in range(2):
            s=lines[i][k]
            e=s+1
            cnt=0
            for j in range(i,N):
                start,end=lines[j]
                if (start <= s and s <= end) or\
                    (start < e and e <= end) or\
                    (s <= start and end <= e):
                    cnt+=1
            answer=max(answer,cnt)
        
    return answer

solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
])
solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
])
solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])