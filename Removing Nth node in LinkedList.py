class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next =next
class LinkedList:
    def __init__ (self):
        self.head = None
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
    #Returning the length of a Linked list
    def get_l(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    #Inserting a New List of Values
    def insert_Values(self,data_list):
        self.head=None
        for l in data_list:
            self.insert_at_end(l)
    def removeNthFromEnd(self, n):
        l=[]
        itr=self.head
        while itr:
            l.append(itr.data)
            itr=itr.next
        l.pop(len(l)-n)
        i=Node()
        temp = i
        for j in l:
            i.next = Node(j)
            i = i.next
        return temp.next


if __name__=="__main__":
    m_l=LinkedList()
    m_l.insert_at_end(1)
    m_l.insert_at_end(2)
    m_l.insert_at_end(3)
    m_l.insert_at_end(4)
    m_l.insert_at_end(5)
    m_l.print()
    m_l.removeNthFromEnd(2)
    m_l.print()

