class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = -1,len(nums)-1
        while l+1 < r:
            m = (l+r)//2
            if nums[m] > nums[-1]:
                l = m
            else:
                r = m
        return nums[r]


        