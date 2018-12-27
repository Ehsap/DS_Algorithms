# Min heap implementation
import unittest

class MinHeap:
    def __init__(self):
        self.A = [0]
        self.heap_size = 0
    
    def parent(self, i):
        return i//2
    
    def left(self, i):
        return (2*i) 
    
    def right(self, i):
        return (2*i) + 1

    def insert(self, val):
        self.A.append(val)
        self.percUp(self.heap_size-1)
        self.heap_size += 1

    def getMin(self):
        return self.A[1]
    
    def extractMin(self):
        min_elem = self.A.pop(1)
        self.A.insert(1, self.A.pop())
        self.heap_size -= 1
        self.percDown(1)
        return min_elem
    
    def percDown(self, i):
        while (2*i) <= self.heap_size:
            minChild = self.minChild(i)
            if self.A[i] > self.A[minChild]:
                self.swap(i, minChild)
            i = minChild
    
    def percUp(self, i):
        while self.A[i] < self.A[self.parent(i)] and self.parent(i) > 0:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def minChild(self, i):
        if (2*i) + 1 > self.heap_size:
            return self.left(i)
        else:
            if self.A[self.left(i)] < self.A[self.right(i)]:
                return self.left(i)
            else:
                return self.right(i)
    
    def buildMinHeap(self, A):
        self.A += A
        self.heap_size = len(self.A) - 1 
        i = self.heap_size//2
        while i > 0:
            self.percDown(i)
            i = i - 1
    
class Test(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()
        for i in [5, 9, 11, 14, 7, 19, 21, 33, 17, 27, 18]:
            self.heap.insert(i)

    def test_getMax(self):
        self.heap2 = MinHeap()
        self.heap2.buildMinHeap([5, 9, 11, 14, 7, 19, 21, 33, 17, 27, 18])
        for i in range(self.heap2.heap_size):
            print(self.heap2.extractMin())
        # for i in range(self.heap.heap_size):
        #     print(self.heap.extractMin())
            # self.assertEqual(self.heap.getMin(), min(self.heap.A[1:]))
    
    # def test_extractMax(self):
    #     self.assertEqual(self.heap.extractMax(), 33)
    
    # def test_buildMaxHeap(self):
    #     heap2 = MaxHeap()
    #     A = [5, 4, 66, 3, 2, 1, 12, 33, 24, 25, 26, 100]
    #     heap2.buildMaxHeap(A)
    #     print(heap2.A)

    # def test_heapSort(self):
    #     heap3 = MaxHeap()
    #     A = [10, 9, 8, 7, 6, 5, 1]
    #     heap3.heapsort(A)
    #     A.append(0)
    #     A.reverse()
    #     self.assertEqual(heap3.A, A)

if __name__ == '__main__':
    unittest.main()       