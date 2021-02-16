def Kth_Smallest_number2D(Matrix,k):
    li =[]
        
    for i in range(0,len(matrix)):
        li.extend(matrix[i])
        
    li.sort()
    return li[k-1]

if __name__=='__main__':
    matrix=[[10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [25, 29, 37, 48], 
        [32, 33, 39, 50]]
    k=3
    print(Kth_Smallest_number2D(matrix,k))