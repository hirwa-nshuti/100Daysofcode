class Median:
    def findMedianSortedArrays(self, nums1, nums2):
        new=sorted(nums1+nums2)
        x=len(new)
        if x%2==1:
            return new[int(x/2)]
        elif x%2==0:
            return (new[int(x/2)]+new[int(x/2)-1])/2
if __name__=="__main__":
    a=[1,2]
    b=[3]
    c=[1,283,4577,609]
    d=[98732,4739,21]

    print(Median().findMedianSortedArrays(a,b))
    print(Median().findMedianSortedArrays(c,d))