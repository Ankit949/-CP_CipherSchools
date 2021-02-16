#Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.
def Kth_Smallest_number(arr,k):
    arr.sort() # O(N) complexity
    return arr[:k]

if __name__=='__main__':
    arr=[7, 10, 4, 3, 20, 15]
    k=3
    print(Kth_Smallest_number(arr,k))