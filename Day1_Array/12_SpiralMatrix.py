#Given a 2D array, print it in spiral form

def SpiralMatrix(Matrix):
    row_Sindex=0
    column_Sindex=0
    row_Eindex=len(Matrix)
    column_Eindex=len(Matrix[0])
    
    while (row_Sindex<row_Eindex and column_Sindex<column_Eindex):

        #printing 1st row element
        for i in range(column_Sindex,column_Eindex):
            print(Matrix[row_Sindex][i],end=" ")
        row_Sindex+=1
        #printing last column
        for i in range(row_Sindex,row_Eindex):
            print(Matrix[i][column_Eindex-1],end=" ")
        column_Eindex-=1

        
        if row_Sindex<row_Eindex:
            for i in range(column_Eindex-1,column_Sindex-1,-1):
                print(Matrix[row_Eindex-1][i],end=" ")
            row_Eindex-=1
        if column_Sindex<column_Eindex:
            for i in range(row_Eindex-1,row_Sindex-1,-1):
                print(Matrix[i][column_Sindex],end=" ")
            column_Sindex+=1

if __name__=='__main__':
    Matrix=[[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
    SpiralMatrix(Matrix)