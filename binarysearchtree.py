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
            if node.parent.which(node) == -1:
                node.parent.left = node.left if node.left is not None else node.right
            else:
                node.parent.right = node.left if node.left is not None else node.right
        
        else:
            node.value = self.findmin(node.left).value
            self._delete(self.find(node.value,node.left))
        
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
        print(node.value)
        self.printvalues(node.left)
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
