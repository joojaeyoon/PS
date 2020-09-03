
def solution(board, moves):
    answer = 0
    storage=[-1]

    for m in moves:
        for h in range(len(board)):
            if board[h][m-1]!=0:
                if storage[-1]==board[h][m-1]:
                    storage.pop()
                    answer+=2
                else: storage.append(board[h][m-1])
                board[h][m-1]=0
                break

    return answer


result=solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])

print(result)