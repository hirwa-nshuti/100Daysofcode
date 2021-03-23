"""
Given a string s, remove duplicate letters so that 
every letter appears once and only once. You must
 make sure your result is the smallest in lexicographical 
 order among all possible results.
"""
class remoc:
    def removeDuplicateLetters(self, s):
        d = {c: idx for idx, c in enumerate(s)}
        
        out = []
        
        for idx, c in enumerate(s):
            if c not in out:
                
                while out and idx < d[out[-1]] and c < out[-1]:
                    out.pop()
                    
                out.append(c)
        
        return "".join(out)
print(remoc().removeDuplicateLetters("ababcbsdsbaj"))