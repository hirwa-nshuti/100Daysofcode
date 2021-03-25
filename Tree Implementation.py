"""
Suppose you have a stock that sells Electronics
and you have three different categories ach with its other types
Phonrs: Iphone, Motorola, Google Pixel, Nokia
TVs: Samung, LG, Skyworth
Laptops: MacBook, Lenovo, Microsoft Surface

This products Hierarchy can be presented using tree Data Structure
A tree Data Structure has 3 main parts
Root Node: Electronics
Node: Phones,Laptops and TVs(parents)
Leaf Nodes : Mac,Iphone,LG(Children)
"""
#General Tree Implementation
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    #getting the level of Tree element    
    def get_level(self):
        level = 0
        par = self.parent
        while par:
            level += 1
            par = par.parent 
        return level

    def print_tree(self):
        space = " " * self.get_level() * 4
        if self.parent:
            prefix = space + "|__"
        else:
            prefix = ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_prod_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree() 
    print (tv.get_level())

if __name__ == '__main__':
    build_prod_tree()