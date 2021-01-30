class Threes:
    def threeSum(self, nums):
        lookup = {}
        out = set()
        
        nums=sorted(nums)
        for i, n in enumerate(nums):
            lookup[n] = i
            

        for i, a  in enumerate(nums):
            if (i!=0 and nums[i] == nums[i-1]) : 
                continue
            for j, b in enumerate(nums[i+1:]):
                c = -(a+b)
                if c in lookup and lookup[c] > i and lookup[c] > (j+i+1):
                    out.add((a, b, c))
        return list(out)  

if __name__=="__main__":
    a=[1,-1,0,2,4,-4]
    b=[1,0,-2,5,-6,8,3,-1]
    print(Threes().threeSum(a))
    print(Threes().threeSum(b))
