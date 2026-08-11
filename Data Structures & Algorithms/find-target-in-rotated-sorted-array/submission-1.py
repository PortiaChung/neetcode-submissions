import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums):
            l,r = -1,len(nums)-1
            while l+1<r:
                m = (l+r)//2
                if nums[m] > nums[-1]:
                    l = m
                else:
                    r = m
            return r
        i = findMin(nums)
        if target > nums[-1]:
            j = bisect.bisect_left(nums,target,0,i)
        else:
            j = bisect.bisect_left(nums,target,i,len(nums))
        
        if j < len(nums) and nums[j] == target:
            return j
        return -1
