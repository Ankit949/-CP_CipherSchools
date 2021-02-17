def BalencedCombination(l,open,closed,n,str):
    if len(str)==2*n:
        l.append(str)
    if open<n:
        BalencedCombination(l,open+1,closed,n,str+"{")
    if closed<open:
        BalencedCombination(l,open,closed+1,n,str+"}")
if __name__=="__main__":
    n=3
    l=[]
    str=""
    open=0
    closed=0
    BalencedCombination(l,open,closed,n,str)
    for i in l:
        print(i)