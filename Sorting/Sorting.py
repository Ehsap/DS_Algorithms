import sys

def insertionSort(arr):
    for i in range(len(arr)-1):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr 

def quicksort(arr):
    left = []
    equal = []
    right = []

    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                right.append(i)
        return quicksort(left) + equal + quicksort(right)
    else:
        return arr 
       
def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        leftHalf = A[:mid]
        rightHalf = A[mid:]

        print("LEFT")
        print(leftHalf)
        print("RIGHT")
        print(rightHalf)
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0
        
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                A[k] = leftHalf[i]
                i += 1
            else:
                A[k] = rightHalf[j]
                j += 1
            k += 1
        
        while i < len(leftHalf):
            A[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            A[k] = rightHalf[j]
            j += 1
            k += 1
        print("MERGED") 
        print(A)
        

def test_mergesort():
    a = [2, 9, 0, 1, 5, 6, 7, 3]
    b = [1]

    mergeSort(a)
    mergeSort(b)
    print(a)
    print(b)

def heapsort(arr):
	pass 

    #       2 9 0 1 5 6 7 3
    #   2 9 0 1         5 6 7 3
#     2 9     01       5 6    7 3
#    2   9   0   1    5   6   7   3