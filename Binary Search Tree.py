"""
Like when implementing sets in python
Every Node has at most 2 Child Nodes(Binary Tree)
In Binary Search Tree Every node has a certain rule to follow
In BST left search tree<currNode and right>currNode
and also elements are unique not duplicated
Search Complexity = O(log n)
Insertion Complexity = o(log n)

*Breadth first Search
*Depth first search: In order traversal,Pre order Traversal, Post order traversal
 
"""
#Defining a Binary Search Tree Class
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            #Add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            #Add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elemen = []
        #Visit Left first
        if self.left:
            elemen += self.left.in_order_traversal()
        #Check the base Node
        elemen.append(self.data)

        #Visiting the right 
        if self.right:
            elemen += self.right.in_order_traversal()

        return elemen
    def search(self,val):
        if self.data == val :
            return True
        if val <self.data:
            #val likely to be in left
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data :
            #Val likely to be in right
            if self.right: 
                return self.right.search(val)
            else:
                return False
    def pre_order_traversal(self):
        elements = []
        #Check the base Node
        elements.append(self.data)
        #Check the left subtree
        if self.left:
            elements += self.left.pre_order_traversal()
        #Check the right
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    def post_order_traversal(self):
        elements = []
        #First Checking the left subtree
        if self.left:
            elements += self.left.post_order_traversal()
        #Cheching the right subtree
        if self.right:
            elements += self.right.post_order_traversal()
        #Checking the base Node
        elements.append(self.data)

        return elements

    def find_min(self):
        #Checking if we have left subtree as min has to be on left
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        #Checking if we have right subtree as max has to be on right
        if self.right is None:
            return self.data  
        return self.right.find_max()  
    def calc_sum(self):
        #Summing all left subtree elements
        if self.left:
            sum_left = self.left .calc_sum()
        else:
            sum_left = 0
        #Summing all right Subtree Elements
        if self.right:
            sum_right = self.right .calc_sum()
        else:
            sum_right = 0

        return self.data + sum_left + sum_right



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range (1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    num_tree = build_tree(nums)
    print("Entered Numbers: ", nums)
    print("Minimum: ",num_tree.find_min())
    print("MAximum: ", num_tree.find_max())
    print("Sum: ", num_tree.calc_sum())
    print("In order traversal: ",num_tree.in_order_traversal())
    print("pre order traversal: ",num_tree.pre_order_traversal())
    print("post order traversal: ",num_tree.post_order_traversal())