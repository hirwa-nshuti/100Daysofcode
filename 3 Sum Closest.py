"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest
 to target. Return the sum of the three integers. 
 You may assume that each input would have exactly 
 one solution.
 Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the 
target is 2. (-1 + 2 + 1 = 2).
"""
class sumclose:
    def threeSumClosest(self, nums, target):
        size = len(nums)
        if size == 3:
            return sum(nums)
        nums.sort()
        curr = sum(nums[:3])
        if curr >= target:
            return curr
        curr = sum(nums[-3:])
        if curr <= target:
            return curr
	
        minsum = 10001
        for i in range(0, size - 2):
            if i!=0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = size - 1
            while(left < right):
                csum = nums[i] + nums[left] + nums[right]
                if abs(minsum - target) > abs(csum - target):
                    minsum = csum
                if csum == target:
                    return target
                if csum < target:
                    left += 1
                elif csum > target:
                    right -= 1
        return minsum 
nums = [-1,2,1,-4]
target = 1
print(sumclose().threeSumClosest(nums,target))