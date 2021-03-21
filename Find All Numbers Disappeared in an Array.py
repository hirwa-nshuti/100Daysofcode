"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do
 not appear in this array.

 Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Missarr:
    def findDisappearedNumbers(self, nums):
        num_len = len(nums)
        nums = list(set(nums))
        result = [i for i in range(1, num_len + 1)]
        return list(set(result) - set(nums))
a=[4,3,2,7,8,2,3,1]
print(Missarr().findDisappearedNumbers(a))