#Two People meet each other
def Meet(x1,x2,v1,v2):
    if x1>x2 and v1>=v2:
        return False
    if x1<x2 and v1<=v2:
        return False
    #use the concept of relative velocity
    if abs(x1-x2)%abs(v1-v2)==0:
        return True
    else:
        False
if __name__=='__main__':
    x1,v1,x2,v2=5,8,7,4
    if Meet(x1,x2,v1,v2):
        print("Yes")
    else:
        print("NO")