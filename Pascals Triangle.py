"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""
class Pasc:
    def generate(self, numRows):
        out = []    
        for row in range(numRows):
            
            psres = [1]*(row+1)
            
            if len(psres) >= 3:
                for pos in range(1, len(psres)-1):
                    psres[pos] = out[-1][pos-1] + out[-1][pos]
                
            out.append(psres)
            
        return out

n=5
print(Pasc().generate(n))
            