class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else: # find the next available node
                self._insert_recursive(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)
        else:
            return # binary search tree should not have duplicates

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root) #private method that only belongs to the insert method