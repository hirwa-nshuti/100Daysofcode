"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Input: s = "anagram", t = "nagaram"
Output: true
"""
"""
Python One liner:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (Counter(s)==Counter(t))
"""
import sys
class Anagram:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        apper = dict()
        for chars, chart in zip(s, t): 
            apper[chars] = apper.get(chars, 0) + 1
            apper[chart] = apper.get(chart, 0) - 1
        return all(v == 0 for v in apper.values())
a="anagram"
b="nagaram"
c="rat"
d="car"
print(Anagram().isAnagram(a,b))
print(Anagram().isAnagram(c,d))