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

    def __cmp__(self,other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        else:
            return 0