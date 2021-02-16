class lcase:
    def letterCasePermutation(self, S):
        S= S.lower() 
        n= len(S)
        out = []
        def assist(i,A):
            if i==n:
                return out.append(''.join(A))
            x   = S[i]
            arr = [x,x.upper()] if x.isalpha() else [x]
            for e in arr:
                A.append(e)
                assist(i+1,A)
                A.pop()
        assist(0,[])
        return out  
a="a1b2"
b="1234"
c="swg124"
print(lcase().letterCasePermutation(a)) 
print(lcase().letterCasePermutation(b)) 
print(lcase().letterCasePermutation(c)) 