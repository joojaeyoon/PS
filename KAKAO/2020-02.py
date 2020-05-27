class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root

        while word:
            if word[0] not in cur:
                cur[word[0]] = {}
            cur = cur[word[0]]
            word = word[1:]
        cur[0] = {}

    def getCurs(self, curs, char):

        new_curs = []

        if char == "?":
            for c in curs:
                new_curs += [c[key] for key in c.keys()]
        else:
            for c in curs:
                if char not in c:
                    continue
                new_curs += [c[char]]

        return new_curs

    def find(self, word):
        curs = [self.root]
        count = 0

        while word:
            curs = self.getCurs(curs, word[0])
            word = word[1:]

        for c in curs:
            if 0 in c:
                count += 1

        return count


def solution(words, queries):
    answer = [0 for _ in range(len(queries))]

    trie = Trie()

    for word in words:
        trie.insert(word)

    for i, query in enumerate(queries):
        answer[i] = trie.find(query)

    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
