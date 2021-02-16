#Given an array of integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.


def AlternativeSorting(arr):
    arr.sort() #O(nlogn) complexity
    l=0
    r=len(arr)-1

    while(l<r):
        print(arr[r],end=" ")
        print(arr[l],end=" " )
        l=l+1
        r=r-1


if __name__=='__main__':
    arr=[1, 6, 9, 4, 3, 7, 8, 2]
    AlternativeSorting(arr)
