#Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity
#The bruteforce approch is to traverse all the element and check whether it is equal to x or not . Complexity O(n^2)
#optimal approch is by devide and conquer 
def SearchInSorted(matrix,x):
    i=0
    j=3
    while(j>=0 and i!=4):
        if matrix[i][j]<x:
            i=i+1
        elif matrix[i][j]>x:
            j=j-1
        elif matrix[i][j]==x:
            return (i,j)
    return 'Not Found'


if __name__=="__main__":
    matrix=[ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]
    print(SearchInSorted(matrix,38))
        

