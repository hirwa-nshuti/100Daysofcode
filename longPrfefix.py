class Prefix:
    def longestCommonPrefix(strs) :
      
        if len(strs) == 0: 
            return ""
        
        mini_length = len(strs[0])
        
        
        for i in range(1,len(strs)):
           
            if mini_length > len(strs[i]): mini_length= len(strs[i])
   
            for k in range(0,mini_length):
                
                if strs[0][k] != strs[i][k]:
                    
                    mini_length = k
                    
                    break
                    
        return strs[0][0:mini_length]
print(Prefix.longestCommonPrefix(["dog","racecar","car"]))
print(Prefix.longestCommonPrefix([]))
print(Prefix.longestCommonPrefix([""]))
print(Prefix.longestCommonPrefix(["flower","flow","flight"]))
print(Prefix.longestCommonPrefix(["abadf","abasore", "abaantu"]))