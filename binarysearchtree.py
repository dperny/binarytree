from binarynode import Node

class BinarySearchTree():
    """Python3 class for a binary search tree
"""
    def __init__(self):
        self._root = None
        self.size = 0

    def insert(self,value):
        node = Node(None,value,None)
        if self.size == 0:
            self._root = node
        else:
            self._place(node,self._root)
            self.size += 1
        

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

    def find(self,value,node = None):
        if node is None:
            walk = self._root
        else:
            walk = node

        while walk is not None:
            if value == walk.value:
                return walk
            elif value > walk.value:
                walk = walk.right
            else:
                walk = walk.left
        return None

    def delete(self,value,node = None):
        if node is None:
            node = self._root

        #find the node to delete
        node = find(value,node)
        # if the node is a leaf
        if node.left is None and node.right is None:
            # just delete it (make it None)
            node = None
            return

        #if one branch is none, link past the node to its subtree
        elif node.left is None:
            node = node.right
            return
        elif node.right is None:
            node = node.left
            return

        #else the node has two branches
        else:
            node.value = findmax(node).value
            self.delete(node.value,node.left)

        self.size -= 1

    def findmax(self,node = None):
        if node is None:
            node = self._root
        while node.right is not None:
            node = node.right
        return node

    def findmin(self,node = None):
        if node is None:
            node = self._root
        while node.left is not None:
            node = node.left 
        return node

        