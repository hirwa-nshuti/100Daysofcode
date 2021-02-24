'''
Given a balanced parentheses string S, compute the 
score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

Input: "()"
Output: 1
'''
class Score:
	def scoreOfParentheses(self, S):
		return self.helper(S,0,len(S)-1)        
	def helper(self,S,l,r):
		if r-l==1:
			return 1
		count=0
		for i in range(l,r):
			if S[i]=='(':
				count+=1
			if S[i]==')':
				count-=1
			if count==0:
				return self.helper(S,l,i)+self.helper(S,i+1,r)
		return 2*self.helper(S,l+1,r-1)

x="((()))"
print(Score().scoreOfParentheses(x))