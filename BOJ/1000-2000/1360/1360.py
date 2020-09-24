N=int(input())
answer=""
cmd=[]

for i in range(N):
    cmd.append(input().split()+[True])

for i in range(N-1,-1,-1):
    if not cmd[i][3]:
        continue
    if cmd[i][0]=="undo":
        c,t,time,b=cmd[i]
        t,time=int(t),int(time)
        
        idx=i
        while idx >= 0:
            if int(cmd[idx][2]) >= time-t:
                cmd[idx][3]=False
            else:
                break
            idx-=1

for c in cmd:
    if c[3]:
        answer+=c[1]

print(answer)