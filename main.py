from binarysearchtree import *
from binarynode import *
import sys
import subprocess

class interpreter:
    def __init__(self,filename):
        self.store = BinarySearchTree()
        self._filename = filename
    
    def cinput(self,action):
        action = action.split(" ")
        if action[0] == "i":
            self.insert(int(action[1]))
        elif action[0] == "f":
            self.find(int(action[1]))
        elif action[0] == "d":
            self.delete(int(action[1]))
        elif action[0] == "t":
            self.test()
        elif action[0] == "s":
            self.swap(int(action[1]),int(action[2]))
        elif action[0] == "v":
            self.visualize()
        elif action[0] == "r":
            self.rotate()
        
    def insert(self,value):
        self.store.insert(value)
        print("{0} was inserted!".format(value))
    
    def find(self,value):
        if self.store.find(value) is not None:
            print("value is in tree!")
        else:
            print("value is not in tree!")
    
    def delete(self,value):
        self.store.delete(value)
        print("{0} was deleted!".format(value))
    
    def test(self):
        if self.store.verify():
            print("tree is not broken")
        else:
            print("tree is broken")
    
    def swap(self,value,fault):
        self.store.find(value).value = fault
        self.t()

    def visualize(self):
        self.store.graphviz(self._filename)
        subprocess.call("dot -Tpng -O " + self._filename,shell=True)
        subprocess.call("eog "+self._filename+".png",shell=True)

    def rotate(self,value):
        self.store.rotate(value)
        


def main(filename):
    cli = interpreter(filename)
    while True:
        cli.cinput(input("> "))

if __name__ == '__main__':
    main(sys.argv[1])
