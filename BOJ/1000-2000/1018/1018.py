import sys

N,M=map(int,input().split())

board=[]
w_board=["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW",
        "WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
b_board=["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB",
        "BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]

for _ in range(N):
    board.append(sys.stdin.readline()[:-1])

answer=50*50

for i in range(N-7):
    for j in range(M-7):
        cnt1=0
        cnt2=0        
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != w_board[k][l]:
                    cnt1+=1
                elif board[i+k][j+l] != b_board[k][l]:
                    cnt2+=1
        answer=min(answer,cnt1,cnt2)

print(answer)