"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]
"""

class PSc:
    def Checkrow(self, rowIndex: int) :
        row = [1] * (rowIndex+1)
        if rowIndex == 0: return row
        prev_row = self.Checkrow(rowIndex-1)
        for i in range(1, len(row)-1):
            row[i] = prev_row[i-1] + prev_row[i]
        return row  

index=4
print(PSc().Checkrow(index))   