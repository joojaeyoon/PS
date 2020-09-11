# Programmers LV 3 입국심사

def solution(n, times):
    answer = -1
    times.sort()

    lo = 0
    hi = times[-1]*n

    while lo <= hi:
        mid = (lo+hi)//2
        cnt = 0

        for time in times:
            cnt += mid//time

        if cnt >= n:
            if answer == -1:
                answer = mid
            else:
                answer = min(answer, mid)
            hi = mid-1
        elif cnt < n:
            lo = mid+1

    return answer


print(solution(6, [7, 10]))
