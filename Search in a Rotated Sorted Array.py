'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k
(0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1],
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and 
become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if 
it is in nums, or -1 if it is not in nums.
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
class Serotred:
    def search(self, nums, target):
        res = []
        for i in range(0, len(nums)):
            if nums[i] == target:
                res.append(i)
                pass
        if len(res) == 1:
            return res[0]
        else:
            return -1 
nums =[4,5,6,7,0,1,2] 
target = 3
num = [4,5,6,7,0,1,2] 
targ = 0
print(Serotred().search(nums,target))
print(Serotred().search(num,targ))