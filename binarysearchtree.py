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
        
    def printvalues(self,node = -1):
        if node is None:
            return
        if node == -1:
            node = self._root
        print(node.value)
        self.printvalues(node.left)
        self.printvalues(node.right)
    
    def verify(self):
        array = []
        return self._verify(self._root,self.findmin(),self.findmax())
    
    def _verify(self,node,min,max):
        if node is None:
            return True
        
        return node.value > min.value and \
               node.value < max.value and \
               self._verify(node.right,node.value,max) and \
               self._verify(node.left,min,node.value)
    
    def graphviz(self,filename):
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