"""
Implementing some of the LinkedList functions 
In this file I try to practice on how to play with Linkedlists and thsi makes me more Familiar with
Linkedlists
"""
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next =next
class LinkedList:
    def __init__ (self):
        self.head = None
    #Inserting the Linkedlist values at the begining
    def insert_at_beginiing(self,data):
        node=Node(data,self.head)
        self.head=node
    #Function to print the Linkedlist
    def print(self):
        if self.head is None:
          print("Empty LinkedList")
          return
        iterator=self.head
        lstr=""
        while iterator:
            lstr+=str(iterator.data)+"-->"
            iterator=iterator.next
        print(lstr)

    #Inserting Values at the end
    def insert_at_end(self,data):
        if self.head is None:
          self.head=Node(data,None)
          return
        itr=self.head
        while itr.next:
              itr = itr.next
        itr.next=Node(data,None)
    #Inserting a New List of Values
    def insert_Values(self,data_list):
        self.head=None
        for l in data_list:
            self.insert_at_end(l)

    #Returning the length of a Linked list
    def get_l(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    #Removing Element at a given Index
    def remove_el(self,index):
        if index<0 or index>=self.get_l():
            raise Exception("Index Out of range")
        if index ==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr = itr.next
            count +=1

    #Inserting a Certain value at a given Index
    def insert_at_ind(self,index,data):
        if index<0 or index>=self.get_l():
            raise Exception("Index Out of range")
        if index==0:
            self.insert_at_beginiing(data)
            return
        count=0
        itr=self.head
        while itr:
            if count ==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1
    #Inserting a value after a certain value
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    #Removing Data by Value
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    



        

if __name__=="__main__":
    my_list = LinkedList()
    my_list.insert_Values(["Nshuti","colors","greatest"])
    my_list.remove_el(0)
    my_list.insert_at_ind(1,"Hirwa")
    my_list.insert_at_end(100)
    my_list.insert_at_beginiing(3)
    my_list.print()
    print("Length of my Linkedlist is ",my_list.get_l())     
