class Node:
    """node class for python.

    can be used for all sorts of link-y things
    """

    def __init__(self,left,value,right,parent=None):
        self.left = left
        self.right = right
        self.value = value
        # use with trees
        self.parent = parent

    def which(self,node):
        if node is self.left:
            return -1
        elif node is self.right:
            return 1
        else:
            return 0