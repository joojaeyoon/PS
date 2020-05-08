def solution(snapshots, transactions):
    answer = []
    t_id = []
    accounts = {}

    for acc in snapshots:
        accounts[acc[0]] = int(acc[1])

    for tr in transactions:
        if tr[0] not in t_id:
            t_id.append(tr[0])

            if accounts.get(tr[2], None) == None:
                accounts[tr[2]] = 0
            if tr[1] == "SAVE":
                accounts[tr[2]] += int(tr[3])
            else:
                accounts[tr[2]] -= int(tr[3])

    for k, v in zip(accounts.keys(), accounts.values()):
        answer.append([k, v])

    return answer


snap = [
    ["ACCOUNT1", "100"],
    ["ACCOUNT2", "150"]
]

tran = [
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["2", "WITHDRAW", "ACCOUNT1", "50"],
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["4", "SAVE", "ACCOUNT3", "500"],
    ["3", "WITHDRAW", "ACCOUNT2", "30"]
]


solution(snap, tran)
