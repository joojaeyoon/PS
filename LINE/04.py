def solution(dataSource, tags):
    docs = []

    for data in dataSource:
        count = 0
        for tag in tags:
            if tag in data:
                count += 1
        if count != 0:
            docs.append([data[0], count])

    for i in range(len(docs)-1):
        for j in range(i+1, len(docs)):
            if docs[i][1] < docs[j][1] or (docs[i][1] == docs[j][1] and docs[i][0] > docs[j][0]):
                docs[i], docs[j] = docs[j], docs[i]

    answer = [doc[0] for doc in docs][:10]

    return answer


ds = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

ts = ["t1", "t2", "t3"]

solution(ds, ts)


#  ["doc1", "doc2", "doc4", "doc3"]
