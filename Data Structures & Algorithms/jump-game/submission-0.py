class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i,x in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx,i+x)
        return True

        
        