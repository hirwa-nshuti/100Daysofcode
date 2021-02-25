class Short:
    def findUnsortedSubarray(self, nums):
        sortNums = sorted(nums)
        if sortNums == nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i] != sortNums[i]:
                firstMismatch = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sortNums[j]:
                lastMismatch = j
                break
        
        return lastMismatch - firstMismatch + 1       


a=[2,6,4,8,10,9,15]
print(Short().findUnsortedSubarray(a))