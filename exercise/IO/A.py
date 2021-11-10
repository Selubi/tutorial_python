def get_adj(index,W,H):
    a=[]
    if(index!=0):
        a.append(index-W)
    if(index%W!=0):
        a.append(index-1)
    if(index%W!=W-1):
        a.append(index+1)
    if(index<H*W-W):
        a.append(index+W)
    return a
H,W=map(int,input().split())
M=[j for i in range(H) for j in list(input())]
start=M.index('s')
S=[False for i in range(H*W)]
S[start]=True
F=get_adj(start,W,H)
ans=False
while F:
    now=F.pop()
    if(M[now]=='#' or S[now]):
        continue
    if(M[now]=='g'):
        ans=True
        break
    else:
        S[now]=True
        F.extend(get_adj(now,W,H))
if(ans):
    print("Yes")
else:
    print("No")

