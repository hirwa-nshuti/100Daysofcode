'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
class Long:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ''
        l_max, offset = 0, 1
        for i in range(len(s)):
            l, r = i, i

            while r < len(s) - 1 and s[l] == s[r+1]:
                r += 1

            while 0 <= l and r < len(s) and s[l] == s[r]:
  
                if r+1 - l > offset:
                    offset, l_max = r+1 - l, l
                r += 1
                l -= 1
        return s[l_max: l_max + offset]
a="babad"
print(Long().longestPalindrome(a))