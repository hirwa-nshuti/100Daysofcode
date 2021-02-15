'''
Given a m * n matrix mat of ones (representing soldiers) and zeros 
(representing civilians), return the indexes of the k weakest 
rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in 
row i is less than the number of soldiers in row j, or 
they have the same number of soldiers but i is less than j. 
Soldiers are always stand in the frontier of a row, that is, 
always ones may appear first and then zeros.
'''
class Weak:
    def kWeakestRows(self, mat, k):
          
        soldiers = {}
        
        for i in range(len(mat)):
            soldiers[i] = mat[i].count(1)
            
        soldiers = dict(sorted(soldiers.items(), key=lambda x:x[1]))
        
        return [x for x in soldiers.keys()][:k]

a=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k=3
print(Weak().kWeakestRows(a,k))
   