# Programmers LV 3 여행 경로

answer = ""
target = 0


def dfs(now, route, routes, visited):

    if len(route) == target:
        global answer
        if answer > route or answer == "":
            answer = route
        return

    if not routes.get(now, False):
        return

    for i, r in enumerate(routes[now]):
        if not visited[now][i]:
            visited[now][i] = True
            dfs(r, route+" "+r, routes, visited)
            visited[now][i] = False


def solution(tickets):
    global answer
    global target

    routes = {}
    visited = {}
    target = (len(tickets)+1)*3+len(tickets)

    for ticket in tickets:
        if not routes.get(ticket[0], False):
            routes[ticket[0]] = []
            visited[ticket[0]] = []
        routes[ticket[0]].append(ticket[1])
        visited[ticket[0]].append(False)

    dfs("ICN", "ICN", routes, visited)

    return answer.split()


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"],
                ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
