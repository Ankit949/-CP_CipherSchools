#You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

def MissingNumber(arr):
    x1=arr[0]
    x2=1

    for i in range(1,len(arr)):
        x1=x1^arr[i]
    for i in range(2,len(arr)+2):
        x2=x2^i
    return x1^x2

if __name__=='__main__':

    arr=[1, 2, 4, 5, 6]
    print(MissingNumber(arr))