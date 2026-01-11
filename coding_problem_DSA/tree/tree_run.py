from collections import deque
from binaryTree import BinaryTree,Node

def main():
    r1=BinaryTree(3)
    r1.left=Node(2)
    r1.right=Node(1)
    r=r1.print_tree()
    print(r1.maxWidth())
   

if __name__=='main':
    main()