class Dup:
    def removeDuplicates(self, nums):
        j = 1
        while j < len(nums):
            if nums[j] == nums[j-1]:
                nums.pop(j-1)
                j-= 1
            j+=1
if __name__ == "__main__":
    a=[]
    print(Dup().removeDuplicates(a))