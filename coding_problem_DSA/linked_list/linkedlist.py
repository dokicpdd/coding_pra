# Node class to represent individual elements
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Reference to the next node

# Linked List class to manage the nodes
#each linkedlist object has a attribute head which is a node object
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize empty list
        
    # Add a node at the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # Add a node at the end
    def add_at_end(self, data):
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return
            
        # Otherwise, traverse to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node

    def length(self):
        le=0
        cur=self.head
        while cur:
            le+=1
            cur=cur.next
        return le
    
    def reverse(self):
        pre =None
        cur=self.head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        self.head=pre 

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def node_forward(self,num):
        cur=self.head
        list_len=self.length()
        # steps we take to /move to where we want to start
        start_pos=int(input('where to start'))

        if start_pos>list_len-1:
            start_pos=start_pos%list_len
        for i in range(start_pos):
                cur=cur.next
        for i in range(num):
            if not cur:
                cur=self.head
            cur=cur.next
        return cur.data

    def mergeTwoLists(self, list1,list2):
        '''
        merge two sorted linkedlist into one single sorted 
        linkedlist; list1 and 2 are the heads of two linkedlist
        '''
        '''
        dummy 和 cur 是两个不同的变量，但它们 “指向同一个地方”。
        对 cur.next 的修改，本质是修改了这个共享对象的 next 属性，因此 dummy 自然能 “看到” 这个变化。

        '''
        dunmmy=Node(0)
        cur=dunmmy
        list1=list1.head
        list2=list2.head
        while list1 and list2:
            if list1.data < list2.data:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        self.head=dunmmy.next