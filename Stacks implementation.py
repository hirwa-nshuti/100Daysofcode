""" For example moving back in browsing data so you can open
the last page you visited using back LIFO(Last in First Out)
Also in any editor where we use undo(Ctrl+Z) we are performing
the stack operation.

push adds the last element accessed
pop removes the last element accessed

Runtime complexity
Push/Pop element: O(1)
Search element by value: O(n)

Stacks in python:
List
Collections.deque
que.LifoQueue
"""

from collections import deque
class stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
#A function to reverse this string "We will win this match"
def rev_st(s):
    stk=stack()
    for char in s:
        stk.push(char)
    reversed_s=""
    while stk.size() >0:
        reversed_s +=stk.pop()
    return reversed_s

if __name__ =="__main__":
    print(rev_st("We will win this match"))
#A function to check the valid parantheses
def check_s(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2
def is_balanced(s):
    data=stack()
    for c in s:
        if c=="[" or c=="{" or c=="(":
            data.push(c)
        if c =="]" or c=="}" or c==")":
            if data.size()==0:
                return False
            if not check_s(c,data.pop()):
                return False
    return data.size()==0 

if __name__=="__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

