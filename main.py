from binarysearchtree import *
from binarynode import *
import sys

class interpreter:
    def __init__(self,filename):
        self.store = BinarySearchTree()
        self._filename = filename
    
    def cinput(self,action):
        action = action.split(" ")
        if action[0] == "i":
            self.i(int(action[1]))
        elif action[0] == "f":
            self.f(int(action[1]))
        elif action[0] == "d":
            self.d(int(action[1]))
        elif action[0] == "t":
            self.t()
        elif action[0] == "s":
            self.s(int(action[1]),int(action[2]))
        elif action[0] == "v":
            self.v()
        
    def i(self,value):
        self.store.insert(value)
        print("{0} was inserted!".format(value))
    
    def f(self,value):
        if self.store.find(value) is not None:
            print("value is in tree!")
        else:
            print("value is not in tree!")
    
    def d(self,value):
        self.store.delete(value)
        print("{0} was deleted!".format(value))
    
    def t(self):
        if self.store.verify():
            print("tree is not broken")
        else:
            print("tree is broken")
    
    def s(self,value,fault):
        self.store.find(value).value = fault
        self.t()

    def v(self):
        self.store.graphviz(self._filename)
        


def main(filename):
    cli = interpreter(filename)
    while True:
        cli.cinput(input("> "))

if __name__ == '__main__':
    main(sys.argv[1])
