from collections import Counter
class Seq:
    def findLHS(self, nums):
        count=Counter(nums)
        out=0
        for i in count:
            if i+1 in count  and count[i+1]+count[i]>out:
                out=count[i+1]+count[i]
        return out  

a=[1,2,3,4,2,2,2]
print(Seq().findLHS(a))