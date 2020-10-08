N = int(input())

words = []
answer = 0

for _ in range(N):
    words.append(input())

counter = {
    chr(ord("A")+i): 0 for i in range(26)
}

for w in words:
    for i in range(len(w)):
        counter[w[i]] += 10**(len(w)-i-1)

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:10]

nums = {}

for i, c in enumerate(counter):
    nums[c[0]] = 9-i

for w in words:
    tmp = ""
    for c in w:
        tmp += str(nums[c])
    answer += int(tmp)

print(answer)
