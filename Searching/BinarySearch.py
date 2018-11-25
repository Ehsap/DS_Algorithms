import unittest
def binarySearch(a, k):
    if len(a) == 0:
        return False
    else:
        mid = len(a)//2
        if a[mid] == k:
            return True
        else:
            if k < a[mid]:
                return binarySearch(a[:mid], k)
            else:
                return binarySearch(a[mid+1:], k)
            

class TestBinarySearch(unittest.TestCase):
    def test_search_single_value_array(self):
        self.assertEquals(binarySearch([1], 1), True)

    def test_search_single_value_not_present_array(self):
        self.assertEquals(binarySearch([1], 2), False)

    def test_search_null_array(self):
        self.assertEquals(binarySearch([], 3), False)
    
    def test_search_present_value(self):
        self.assertEquals(binarySearch([1,2,3,4,5,6], 3), True)
        self.assertEquals(binarySearch([1,2,3,4,5,6], 1), True)
        self.assertEquals(binarySearch([1,2,3,4,5,6], 6), True)
        self.assertEquals(binarySearch([1,2,3,4,5,6], 4), True)
        self.assertEquals(binarySearch([1,2,3,4,5,6], 5), True)
        self.assertEquals(binarySearch([1,2,3,4,5,6], 2), True)
    
    def test_search_nonpresent_value(self):
        self.assertEquals(binarySearch([1,2,3,4,5,6], 12), False)

if __name__ == '__main__':
    unittest.main()
    
