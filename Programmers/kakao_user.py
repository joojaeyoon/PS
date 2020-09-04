def compareId(uid,bid):
    if len(uid)!=len(bid): return False

    for i in range(len(bid)):
        if not (uid[i]==bid[i] or bid[i]=="*"):
            return False
    
    return True            

def select(users,check,idx,selected,result):
    if idx == len(check):
        selected=set(selected)
        if selected not in result:
            result.append(selected)
        return
    
    for i in range(len(check[idx])):
        user=check[idx][i]
        if user not in selected:
            select(users,check,idx+1,selected+[user],result)
            

def solution(user_id, banned_id):
    answer = 0
    check=[[] for i in range(len(banned_id))]
    result=[]

    for j,bid in enumerate(banned_id):
        for i,uid in enumerate(user_id):
            if compareId(uid,bid): check[j].append(i)

    select(user_id,check,0,[],result)

    answer=len(result)

    return answer



# result=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
# print(result==2)
# result=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])
# print(result==2)
result=solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])
print(result==3)