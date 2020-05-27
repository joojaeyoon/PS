import sys

N = int(sys.stdin.readline())

hashmap = {i: 0 for i in range(10001)}

for i in range(N):
    num = int(sys.stdin.readline())

    hashmap[num] += 1

for k, v in hashmap.items():
    for _ in range(v):
        print(k)
