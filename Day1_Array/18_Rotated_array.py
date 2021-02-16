
def BinarySearch(arr,x):
    print(arr)
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        print(mid)
        if arr[mid]==x:
            return "True"
        if x>arr[mid]:
            l=mid+1
        
        else:
            r=mid-1
        print(l,r)
    return "False"
def rotatedArray(arr,x):
    l=0
    r=len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        if arr[mid-1]>arr[mid] and x<arr[0]:
            return BinarySearch(arr[mid:],x)
        elif arr[mid-1]>arr[mid] and x>arr[0]:
            return BinarySearch(arr[:mid],x)
        else:
            l=mid+1
    

if __name__=="__main__":
    arr=[4,5,6,7,8,9,10,1,2,3]
    x=6
    if x==arr[0]:
        print("0")
    else:
        print(rotatedArray(arr,x))


