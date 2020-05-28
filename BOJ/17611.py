# PyPy3

import sys

n = int(input())

points = []

h_max, h_min = -500000, 500000
v_max, v_min = -500000, 500000

result = 0

for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

    h_max, h_min = max(h_max, points[-1][1]), min(h_min, points[-1][1])
    v_max, v_min = max(v_max, points[-1][0]), min(v_min, points[-1][0])

dp = [[0 for _ in range(1000000)] for __ in range(2)]

for i in range(len(points)):
    v_l = min(points[i][0], points[i-1][0])
    v_r = max(points[i][0], points[i-1][0])

    h_l = min(points[i][1], points[i-1][1])
    h_r = max(points[i][1], points[i-1][1])

    for j in range(v_l, v_r):
        dp[0][j] += 1
    for j in range(h_l, h_r):
        dp[1][j] += 1

print(max(max(dp[0]), max(dp[1])))
