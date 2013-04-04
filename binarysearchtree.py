from binarynode import Node

class BinarySearchTree():
    """Python3 class for a binary search tree
"""
    def __init__(self):
        self._root = None
        self.size = 0

    def insert(self,value):
        node = Node(None,value,None)
        if size == 0:
            self._root = node
        else:
            self._place(node,self._root)
        

    def _place(self,node,current):
        if node < current:
            if current.left is None:
                current.left = node
                node.parent = parent
            else:
                self._place(node,current.left)
        else:
            if current.right is None:
                current.right = node
                node.parent = current
            else:
                self._place(node,current.right)

    def find(self,value):
        walk = self._root
        while walk is not None:
            if value == walk.value:
                return walk
            elif value > walk.value:
                walk = walk.right
            else:
                walk = walk.left
        return None

    def delete(self,value):
        
