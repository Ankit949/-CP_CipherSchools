#Given two sorted arrays, the task is to merge them in a sorted manner.

def MergesortedArray(arr1,arr2):
    i=0
    j=0
    k=0
    n=len(arr1)
    m=len(arr2)
    MergeArray=[-1]*(m+n)
    print(MergeArray)
    while(i<n and j<m):
        if arr1[i]<=arr2[j]:
            MergeArray[k]=arr1[i]
            i=i+1
        else:
            MergeArray[k]=arr2[j]
            j=j+1
        k=k+1
    while(i<n):
        MergeArray[k]=arr1[i]
        i=i+1
        k=k+1
    while(j<m):
        MergeArray[k]=arr2[j]
        j=j+1
        k=k+1
    return MergeArray


if __name__=='__main__':
    arr1=[1, 3, 4, 5]
    arr2=[2, 4, 6, 8]
    print(MergesortedArray(arr1,arr2))