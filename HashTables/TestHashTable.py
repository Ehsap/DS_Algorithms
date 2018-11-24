import unittest
from HashTable import HashTable

class myTest(unittest.TestCase):

    def test_hash_same_slot(self):
        h = HashTable()
        h.put(0, "A")
        h.put(11, "B")
        h.put(22, "C")
        self.assertEquals(h.contains(0), True)
        self.assertEqual(h.contains(11), True)
        self.assertEqual(h.contains(22), True)

    def test_hash_different_slot(self):
        h = HashTable()
        h.put(0, "A")
        h.put(1, "B")
        self.assertEqual(h.contains(0), True)
        self.assertEqual(h.contains(1), True)
    
    def test_nonexistent_key(self):
        h = HashTable()
        self.assertEqual(h.contains(12), False)
        self.assertEqual(h.get(12), False)
    
    def test_get_values_from_key(self):
        h = HashTable()
        h.put(0, "A")
        h.put(11, "B")
        h.put(22, "C")
        self.assertEqual(h.get(0), "A")
        self.assertEqual(h.get(11), "B")
        self.assertEqual(h.get(22), "C")

    def test_delete_key_no_chaining(self):
        h = HashTable()
        h.put(0, "A")
        h.delete(0)
        self.assertEqual(h.contains(0), False)
        self.assertEqual(h.get(0), False)
    
    def test_delete_last_key_with_chaining(self):
        h = HashTable()
        h.put(0, "A")
        h.put(11, "B")
        h.put(22, "C")
        h.delete(22)
        self.assertEqual(h.contains(22), False)

    def test_delete_first_key_with_chaining(self):
        h = HashTable()
        h.put(0, "A")
        h.put(11, "B")
        h.put(22, "C")
        h.delete(0)
        self.assertEqual(h.contains(0), False)
        self.assertEqual(h.contains(11), True)
        self.assertEqual(h.contains(22), True)

if __name__ == '__main__':
    unittest.main()