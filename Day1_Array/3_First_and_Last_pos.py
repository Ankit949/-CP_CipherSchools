#Find first and last positions of an element in a sorted array
#problem statement:-  Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.


def First_last_pos1(arr,x):
    flag=1
    first=0
    Last=0
    for i in range(len(arr)):
        if arr[i]==x and flag==1:
            first=i
            flag=0
        if arr[i+1]!=x and flag==0:
            Last=i
            break
    print(first,Last)


#Optimised code with O(LogN)

def First_last_pos2(arr,x):
    first=-1
    last=-1
    # first occurance of the number
    left=0
    right=len(arr)-1
    while(left<right):
        mid = left + (right-left)//2
        if arr[mid]==x and arr[mid-1]<x or arr[mid]==x and mid==0:
            first=mid
            break
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    # for last occurance
    left=0
    right=len(arr)-1
    while(left<right):
        mid=left + (right-left)//2
        print(mid)
        if arr[mid]==x and arr[mid+1]>x or arr[mid]==x and mid==len(arr)-1:
            last=mid
            break
        elif arr[mid]>x:
            right=mid-1
        else:
            left=mid+1
    print(first,last)



if __name__=='__main__':
    arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
    x=5
    First_last_pos1(arr,x)
    First_last_pos2(arr,x)

