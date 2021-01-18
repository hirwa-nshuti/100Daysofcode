
class miss:
    def missingNumber(self, nums) -> int:
        #finding the length of nums
        n_l=len(nums)
        
        #Sum of all nums is (n**2+n)/2
        n_sum=int((n_l**2+n_l)/2)
        for num in nums:
            if num>0:
                n_sum=n_sum-num
            
        return n_sum
if __name__=="__main__":
    a=[1,0,3]
    b=[1,2,5,4,0]
    print(miss().missingNumber(a))
    print(miss().missingNumber(b))