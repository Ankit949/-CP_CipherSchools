#Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
#Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
def CountInversion(arr):
 
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                count += 1
 
    return count
 

arr = [1, 20, 6, 4, 5]
n = len(arr)
print(CountInversion(arr))