'''
Given a string and a string dictionary, find the longest 
string in the dictionary that can be formed by deleting 
some characters of the given string. If there are more 
than one possible results, return the longest word with 
the smallest lexicographical order. If there is no possible 
result, return the empty string. 
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
'''
import heapq
class Long:
    def findLongestWord(self, s, d):
        def subsequent(a, b) :
            i = 0
            for c in a:
                if (i := b.find(c, i)) == -1:
                    return False
                i += 1
            return True
        
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            word = heapq.heappop(heap)[1]
            if subsequent(word, s):
                return word
        return '' 
        
s="abpcplea"
d=["ale","apple","monkey","plea"]
print("The longest word is\n:", Long().findLongestWord(s,d))