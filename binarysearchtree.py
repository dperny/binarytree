from binarynode import Node

class BinarySearchTree():
    """Python3 class for a binary search tree
"""
    def __init__(self):
        self._root = None
        self.size = 0

    def insert(self,value):
        """takes in a value to, outputs None"""
        node = Node(None,value,None)
        if self.size == 0:
            self._root = node
        else:
            self._place(node,self._root)
        self.size += 1
        

    def _place(self,node,current):
        if node.value < current.value:
            if current.left is None:
                current.left = node
                node.parent = current
            else:
                self._place(node,current.left)
        else:
            if current.right is None:
                current.right = node
                node.parent = current
            else:
                self._place(node,current.right)

    def find(self,value,node = None):
        """takes in a value to find, returns a node or None if not found"""
        if node is None:
            walk = self._root
        else:
            walk = node

        while walk is not None:
            if value == walk.value:
                self._rotate(walk)
                if walk.parent is None:
                    self._root = walk
                return walk
            elif value > walk.value:
                walk = walk.right
            else:
                walk = walk.left
        return None
    
    def delete(self,value):
        """takes in a value, returns nothing"""
        node = self.find(value)
        if node is not None:
            self._delete(node)
            self.size -= 1
    
    def _delete(self,node):
        if node.left is None or node.right is None:
            if node.parent.left is node:
                if node.left is not None:
                    node.parent.left = node.left
                else:
                    node.parent.left = node.right
            elif node.parent.right is node:
                if node.right is not None:
                    node.parent.right = node.left
                else:
                    node.parent.right = node.right
        else:
            mini = self.findmin(node.right)
            node.value = mini.value
            self._delete(mini)
        
    def findmax(self,node = None):
        """takes in a node, returns the maximum node in that tree

        if no node is provided, searches from root"""

        if node is None:
            node = self._root
        while node.right is not None:
            node = node.right
        return node

    def findmin(self,node = None):
        """takes in a node, returns the minimum node in that tree

        if no node is provided, searches from root"""

        if node is None:
            node = self._root
        while node.left is not None:
            node = node.left 
        return node
        
    def printvalues(self,node = -1):
        if node is None:
            return
        if node == -1:
            node = self._root
        self.printvalues(node.left)
        print(node.value)
        self.printvalues(node.right)
    
    def verify(self):
        """returns True if the tree is correct, else returns False

        should return true unless a node is directly modified"""

        array = []
        return self._verify(self._root,self.findmin().value-1,self.findmax().value+1)
    
    def _verify(self,node,min,max):
        if node is None:
            return True
        if node.value > min \
        and node.value < max \
        and self._verify(node.left,min,node.value) \
        and self._verify(node.right,node.value,max):
            return True
        else: return False
    def graphviz(self,filename):
        """takes in a filename, outputs a graphviz file"""
        outstring = "digraph tree {\n" 
        outstring = outstring + self._graphmap(self._root,"") + "}"
        with open(filename,'w') as fp:
            fp.write(outstring)

    def _graphmap(self,node,string):
        lstring = ""
        rstring = ""
        if node.left is not None:
            lstring = ( 
            '\t"{0}" -> "{1}"\n'.format(node.value,node.left.value) 
            + self._graphmap(node.left,string))

        if node.right is not None:
            rstring = (
            '\t"{0}" -> "{1}"\n'.format(node.value,node.right.value)
            + self._graphmap(node.right,string))

        return string + lstring + rstring

    def rotate(self,value):
        """rotates the node with value to the root position"""
        node = self.find(value)
        while node is not self._root:
            self._rotate(node)

    def _rotate(self,pivot):
        if pivot.parent is None:
            self._root = pivot
            return

        # do a right rotation
        if pivot is pivot.parent.left:
            # save a reference to the parent node
            root = pivot.parent

            # the left node of the parent node
            # becomes the right node of the pivot node
            root.left = pivot.right
            if root.left is not None: root.left.parent = root

            # the right node of the pivot node becomes root
            pivot.right = root
            pivot.parent = root.parent
            root.parent = pivot

        # do a left rotation
        elif pivot is pivot.parent.right:
            # save a reference to the parent node
            root = pivot.parent

            # the right node of the parent node
            # becomes the left node of the pivot node
            root.right = pivot.left
            if root.right is not None: root.right.parent = root

            # the left node of the pivot node becomes root
            pivot.left = root
            pivot.parent = root.parent
            root.parent = pivot

        if pivot.parent is not None:
            if pivot.parent.left is root: pivot.parent.left = pivot
            else: pivot.parent.right = pivot
