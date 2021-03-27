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
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left =self.left.delete(val)

        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else: 
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.left
            elif self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right.delete(min_val)

        return self
         
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range (1,len(elements)):
        root.add_child(elements[i])
    return root    
if  __name__ =="__main__":
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    num_tree = build_tree(nums)
    num_tree.delete(20)
    num_tree.delete(9)
    print("After Deletion: ",num_tree.in_order_traversal())