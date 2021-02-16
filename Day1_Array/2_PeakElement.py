#Find Peak Elelemt
# Peak Element :- The element which is not smaller than its neighbour.
#BruteForce approch is of O(N)
#optimised is of O(LogN) using Binary search

def PeakElement(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        mid=left+(right-left)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            print(arr[mid])
            break
        elif arr[mid]<arr[mid+1]:
            left=mid+1
        else:
            right=mid-1

if __name__=='__main__':
    arr=[10, 20, 15, 2, 23, 90, 67]
    PeakElement(arr)
