#Defining a hash function
"""def get_hash(key):
    h=0
    for char in key:
        h += ord(char)
    return h%100
print(get_hash("hirwa"))
"""

#Creating a hash Table class
class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    #Adding Key values to the Hashtable
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h]=val    
    #Function to get the hash table
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    #Deleting Item from a hashtable
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h] =None


test=Hashtable()
test["march 6"]=130
test["coding"]=263
test["march 17"]=102
print(test["march 6"])
print(test["march 6"])
