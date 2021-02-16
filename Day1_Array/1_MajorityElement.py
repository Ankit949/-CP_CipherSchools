# majority Element :- The number which occur for more than n/2 times
#using Moore Algorithm in O(N)

def MajorityElement(arr):

    candidate=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]== candidate and count!=0:
            count=count+1
        elif arr[i]!=candidate and count!=0:
            count=count-1 
        else:
            candidate=arr[i]
            count=1
    if count==0:
        print("No Majority Elemnet")
    else:
        a=arr.count(candidate)
        if len(arr)//2<a:
            print(candidate)
if __name__=='__main__':
    arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
    MajorityElement(arr)



