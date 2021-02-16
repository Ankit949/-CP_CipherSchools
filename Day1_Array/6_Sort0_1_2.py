#Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last
#This problem can be solved using two method with a complexity of O(n) and O(1) space.

#1st Three pionter approch

def Using_Three_Pointer(arr):
    op=0
    onp=0
    tp=len(arr)-1
    while(onp<tp and op<tp):
        if arr[op]==0:
            op=op+1
        if arr[onp]==1 or (arr[onp]==0 and onp<=op):
            onp=onp+1
        if  arr[tp]==2:
            tp=tp-1
        print(op,tp)
        if arr[op]!=0 and arr[tp]!=2:
            arr[op],arr[tp]=arr[tp],arr[op]
        if arr[onp]!=1 and arr[tp]!=2:
            arr[onp],arr[tp]=arr[tp],arr[onp]
        if arr[op]!=0 and arr[onp]!=1 and op>onp:
            arr[op],arr[onp]=arr[onp],arr[op]

    return arr


if __name__=='__main__':
    arr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]      
    print(Using_Three_Pointer(arr))  

        