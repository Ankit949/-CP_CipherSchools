#You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.


def Segregate(arr):
    op=0
    onp=len(arr)-1

    while(op<onp):
        if arr[op]==1 and arr[onp]==0:
            arr[op],arr[onp]=arr[onp],arr[op]
            op=op+1
            onp=onp-1
            continue
        elif arr[op]==0:
            op=op+1
        elif arr[onp]==1:
            onp=onp-1
    return arr
if __name__=='__main__':
    arr=[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    print(Segregate(arr))