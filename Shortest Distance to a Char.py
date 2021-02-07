'''
Given a string s and a character c that occurs in s, return
 an array of integers answer where answer.length == s.length 
and answer[i] is the shortest distance from s[i] 
to the character c in s.
'''

class Character:
    def shortestToChar(self, s,c):
        out = []
        s = 'A'+s
        match = 0
        for i in range(len(s)):
            out.append(i-match)
            if s[i] == c:
                if match == 0:
                    out[0::] = out[i::-1]
                else :
                    out[(i + match)//2+(i + match)%2:] = out[(i + match)//2:match-1:-1]
                match = i
        return out[1:]
char1="codingisgreat"
b="s"
char2="aaaaaaaaaaaaaabnnsjweeeowoklssljwl"
c="b"
print(Character().shortestToChar(char1,b))
print(Character().shortestToChar(char2,c))