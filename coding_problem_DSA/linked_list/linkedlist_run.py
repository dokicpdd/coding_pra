#from linkedlist import LinkedList
from linkedlist import *
 


if __name__ == "__main__":
    # Create a new linked list
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(0,7):
        l1.add_at_end(i)
        l2.add_at_end(i+1)
    l1.mergeTwoLists(l1,l2)
    l1.print_list()
