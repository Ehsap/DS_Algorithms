import unittest
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = Node()
    
    def insert(self, key):
        if self.root.key is None:
            self.root = Node(key, None, None)
        else:
            self.insert_aux(self.root, key)
    
    def insert_aux(self, root, key):
        if key <= root.key and root.left is None:
            root.left = Node(key, None, None)
        elif key > root.key and root.right is None:
            root.right = Node(key, None, None)
        elif key <= root.key:
            self.insert_aux(root.left, key)
        else:
            self.insert_aux(root.right, key)
    
    def remove(self, key):
        pass

    def search(self, key):
        root = self.root
        while root is not None:
            if key == root.key:
                return True
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return False
    
    def minimum(self):
        root = self.root
        if self.root.key is None:
            return -1
        else:
            while root.left is not None:
                root = root.left
            return root.key
    
    def maximum(self):
        root = self.root
        if self.root.key is None:
            return -1
        else:
            while root.right is not None:
                root = root.right
            return root.key

    def successor(self, key):
        return self.minimum()
        # Find the node
        root = self.root
        while root is not None:
            if key == root.key:
                break
            if key < root.key:
                root = root.left
            else:
                root = root.right
                
         # Minimum of right sub tree
        while root.left is not None:
            root = root.left
        return root.key

    def predecessor(self, key):
        # Maximum of left sub tree
        pass

    def inorder(self):
        return self.inorder_aux(self.root, [])
    
    def inorder_aux(self, root, path):
        if root is not None:
            self.inorder_aux(root.left, path)
            path.append(root.key)
            self.inorder_aux(root.right, path)
        else:
            return []
        return path

    def preorder(self):
        return self.preorder_aux(self.root, [])
    
    def preorder_aux(self, root, path):
        if root is not None:
            path.append(root.key)
            self.preorder_aux(root.left, path)
            self.preorder_aux(root.right, path)
        else:
            return []
        return path 
    
    def postorder(self):
        return self.postorder_aux(self.root, [])
    
    def postorder_aux(self, root, path):
        if root is not None:
            self.postorder_aux(root.left, path)
            self.postorder_aux(root.right, path)
            path.append(root.key)
        else:
            return []
        return path
    

class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(3)
        self.tree.insert(6)
        self.tree.insert(7)
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(9)

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(), [1,2,3,4,5,6,7,9])
    
    def test_preorder(self):
        self.assertEqual(self.tree.preorder(), [5, 4, 3, 1, 2, 6, 7, 9])
    
    def test_postorder(self):
        self.assertEqual(self.tree.postorder(), [2, 1, 3, 4, 9, 7, 6, 5])
    
    def test_search(self):
        self.assertEqual(self.tree.search(8), False)
        self.assertEqual(self.tree.search(5), True)
        self.assertEqual(self.tree.search(3), True)
        self.assertEqual(self.tree.search(2), True)
    
    def test_minimum(self):
        self.assertEqual(self.tree.minimum(), 1)
    
    def test_maximum(self):
        self.assertEqual(self.tree.maximum(), 9)
    


if __name__ == '__main__':
    unittest.main()