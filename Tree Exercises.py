#General Tree Implementation
class TreeNode:
    def __init__(self,name, data):
        self.name =name
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

    def print_tree(self,name_on):
        if name_on == "both":
            value = self.name +" " "(" + self.data +")"
        elif name_on == "name":
            value =self.name
        else:
            value =self.data
        space = " " * self.get_level() * 4
        if self.parent:
            prefix = space + "|__"
        else:
            prefix = ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(name_on)

def build_management_tree():
    #CTO
    Infrastucture_head = TreeNode("Vishwa","Infrastucture Head")
    Infrastucture_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    Infrastucture_head.add_child(TreeNode("Abhijit","App Manager"))

    cto = TreeNode("Chinmay","CTO")
    cto.add_child(Infrastucture_head)
    cto.add_child(TreeNode("Aamir","Application Head"))

    hr = TreeNode("Gels","HR Head")
    hr.add_child(TreeNode("Peter","Recruitment Manager"))
    hr.add_child(TreeNode("Waqas","Policy Manager"))

    ceo = TreeNode("Nilupul","CEO")
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy