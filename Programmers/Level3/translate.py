# Programmers LV 3 단어 변환

from collections import deque

answer = 987654321

def dfs(word, count, words, target, visited):

    if word == target:
        global answer
        answer = min(answer, count)
        return

    for idx, w in enumerate(words):
        c = 0
        for i in range(len(w)):
            if w[i] != word[i]:
                c += 1

        if c == 1 and not visited[idx]:
            visited[idx] = True
            dfs(w, count+1, words, target, visited)
            visited[idx] = False


def solution(begin, target, words):
    global answer
    visited = [False for _ in range(len(words))]

    dfs(begin, 0, words, target, visited)

    if answer == 987654321:
        return 0

    return answer


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
