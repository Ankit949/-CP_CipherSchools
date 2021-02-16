#The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days

def StockProfit(arr):
    min1=arr[0]
    max1=arr[0]
    buying=0
    selling=0
    flag=0
    for i in range(1,len(arr)):
        if arr[i]<min1 and flag==1:
            print(buying,selling)
        if arr[i]<min1:
            flag=0
            min1=arr[i]
            buying=i
        elif arr[i]>max1:
            max1=arr[i]
            selling=i
            flag=1
        if i==len(arr)-1 and flag==1:
            print(buying,selling)
if __name__=='__main__':
    arr=[100, 180, 260, 310, 40, 535, 695]
    StockProfit(arr)


