class Pos:
    def searchRange(self, nums, target):
        def binarysearch(flag):
            ans = -1
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if flag == "LEFT":
                        ans = mid
                        r = mid - 1
                        continue
                    else:
                        ans = mid
                        l = mid + 1
                        continue
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        left = binarysearch("LEFT")
        right = binarysearch("RIGHT")
        
        return [left,right]
a=[5,7,7,8,8,10]
b=8   
print (Pos().searchRange(a,b))