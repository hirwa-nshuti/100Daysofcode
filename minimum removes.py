'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', 
in any positions ) so that the resulting parentheses string is valid
 and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B 
    are valid strings, or
    It can be written as (A), where A is a valid string.
 Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.   
'''
class Min:
    def minRemoveToMakeValid(self, s):
        if len(s)<=0:
            return s
        
        left = []
        id_r = []
        out=''
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c==')':
                if len(left)==0:
                    id_r.append(i)
                else:
                    left.pop()
        s = list(s)
        for i in sorted(id_r+left, reverse=True):
            s.pop(i)
        out=out.join(s)
        return out

a='lee(t(c)o)de)'
print(Min().minRemoveToMakeValid(a))