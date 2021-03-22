#Creating a hash Table class
class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    #Adding Key values to the Hashtable
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found=False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,val)
                found=True
                break
        if not found: 
            self.arr[h].append((key,val))   
    #Function to get the hash table
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        
    #Deleting Item from a hashtable
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                del self.arr[h][index]


test=Hashtable()
test["march 6"]=130
test["coding"]=263
test["march 17"]=102
print(test["march 6"])
print(test["march 17"])
test.__delitem__("march 6")
print(test["march 6"])
print(test["march 17"])