class LinkedList:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class HashTable:
    def __init__(self):
        self.arr = [None] * 11

    def put(self, key, value):
        # Hashes to empty slot
        index = key % 11
        if self.arr[index] is None:
            self.arr[index] = LinkedList(key, value, None)
        # Put value into head of existing linkedlist
        else:
            newHead = LinkedList(key, value, self.arr[index])
            self.arr[index] = newHead
    
    def contains(self, key):
        index = key % 11
        if self.arr[index] is None:
            return False
        else:
            p = self.arr[index]
            while p is not None:
                if p.key == key:
                    return True
                p = p.next
            return False
    
    def get(self, key):
        index = key % 11
        if self.arr[index] is None:
            return False
        else:
            p = self.arr[index]
            while p is not None:
                if p.key == key:
                    return p.val
                p = p.next
            return False
    
    def delete(self, key):
        index = key % 11
        if self.arr[index] is None:
            return False
        else:
            p = self.arr[index]
            if p.key == key:
                self.arr[index] = p.next
                return
            while p.next is not None:
                if p.next.key == key:
                    p.next = p.next.next
                    return
                p = p.next