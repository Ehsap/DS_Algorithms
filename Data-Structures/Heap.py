import unittest

# Max Heap of unlimited size
class MaxHeap:
    def __init__(self):
        self.heap_size = 0 # Number of elements inside the heap
        self.A = [0]

    def parent(self, i):
        return self.A[i//2]

    def parentIndex(self, i):
        return i//2

    def left(self, i):
        return self.A[i*2]

    def leftIndex(self, i):
        return 2*i
    
    def right(self, i):
        return self.A[(2*i) + 1]
    
    def rightIndex(self, i):
        return (2*i) + 1

    def percUp(self, i):
        # Positions a newly added node to its correct place; percolating it upwards
        while self.parentIndex(i) != 0 and self.parent(i) < self.A[i]:
            self.swap(parentIndex=self.parentIndex(i), childIndex=i)
            i = self.parentIndex(i)

    def swap(self, parentIndex, childIndex):
        self.A[parentIndex], self.A[childIndex] = self.A[childIndex], self.A[parentIndex]

    def insert(self, val):
        self.A.append(val) 
        self.percUp(len(self.A) - 1)
        self.heap_size += 1
    
    def getMax(self):
        if self.heap_size == 0:
            raise Exception("No elements in the heap")
        else:
            return self.A[1]
    
    def percDown(self, i):
        # Percolates the root node to its proper position
        while (2*i) <= self.heap_size:
            max_child = self.maxChild(i)
            if self.A[i] < self.A[max_child]:
                self.swap(i, max_child)
            i = max_child

    def maxChild(self, i):
        if (i*2) + 1 > self.heap_size:
            return i * 2
        else:
            if self.A[i*2] > self.A[(i*2)+1]:
                return i*2
            else:
                return (i*2) + 1

    def extractMax(self):
        # Removes and returns the root node. May need to restructure the heap
        # after this is done 
        if self.heap_size == 0:
            raise Exception("Empty Heap")
        else:
            max_elem = self.A.pop(1)
            self.A.insert(1, self.A.pop())
            self.heap_size -= 1
            self.percDown(1)
            return max_elem

    def buildMaxHeap(self, Arr):
        # Constructs a max heap from an unsorted array
        self.A = [0] + Arr
        self.heap_size = len(self.A)-1
        i = len(Arr) // 2
        while i > 0:
            self.percDown(i)
            i = i -1
        
    def heapsort(self, Arr):
        self.buildMaxHeap(Arr)
        arr_length = len(Arr)
        for i in range (arr_length, 1, -1):
            self.A[i], self.A[1] = self.A[1], self.A[i]
            self.heap_size -= 1
            self.percDown(1)


class Test(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()
        for i in [5, 9, 11, 14, 7, 19, 21, 33, 17, 27, 18]:
            self.heap.insert(i)

    def test_getMax(self):
        self.assertEqual(self.heap.getMax(), max(self.heap.A))
    
    def test_extractMax(self):
        self.assertEqual(self.heap.extractMax(), 33)
    
    def test_buildMaxHeap(self):
        heap2 = MaxHeap()
        A = [5, 4, 66, 3, 2, 1, 12, 33, 24, 25, 26, 100]
        heap2.buildMaxHeap(A)
        print(heap2.A)

    def test_heapSort(self):
        heap3 = MaxHeap()
        A = [10, 9, 8, 7, 6, 5, 1]
        heap3.heapsort(A)
        A.append(0)
        A.reverse()
        self.assertEqual(heap3.A, A)

if __name__ == '__main__':
    unittest.main()       