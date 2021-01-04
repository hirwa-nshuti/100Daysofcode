
class Merge:
    def merge(nums1, m, nums2,n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1 
        j =n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1

a=[1,2,3,0,0,0]
m=3
b=[2,5,6]
n=3

print(Merge.merge(a,m,b,n))
print(Merge.merge([1,2,0],2,[1],1))