def maxSubArraySum(a):

    maxsum=0
    Sum=0
    
    for i in range(len(a)):
        if Sum+a[i]<a[i]:
            Sum=0
            Sum=Sum+a[i]
        else:
            Sum=Sum + a[i]
        
        if maxsum<Sum:
            maxsum=Sum
    return maxsum

if __name__=='__main__':
    arr=[3,4 ,5,-2,7,-6,-9,7,8,7,-8]
    print(maxSubArraySum(arr))