# Programmers LV 3 디스크 컨트롤러

from collections import deque
import heapq


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs],
                         key=lambda x: (x[1], x[0])))

    q = []

    heapq.heappush(q, tasks.popleft())
    c_time, total_time = 0, 0

    while len(q) != 0:
        time, start = heapq.heappop(q)
        c_time = max(c_time+time, start+time)
        total_time += c_time-start

        while len(tasks) > 0 and tasks[0][1] <= c_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
        print(q)

    return total_time//len(jobs)


result = solution([[0, 10], [2, 3], [9, 3]])

print(result)
