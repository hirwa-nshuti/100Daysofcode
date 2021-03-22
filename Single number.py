"""
Given a non-empty array of integers nums, every element 
appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear 
runtime complexity and without using extra memory?
Input: nums = [2,2,1]
Output: 1
"""
from collections import Counter
class Sing:
    def singleNumber(self, nums):
        for key, values in Counter(nums).items():
            if(values!=1):
                pass
            else:
                return (key)
num=[2,2,1]
print(Sing().singleNumber(num))