class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = cnt = 0
        for x in nums:
            if x:
                cnt +=1
            else:
                mx = max(mx,cnt)
                cnt = 0
        return max(mx,cnt)
        