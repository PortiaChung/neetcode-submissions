class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 0
        right = max(piles)

        while left+1 < right:
            mid = (left+right)//2
            if sum((p+mid-1)//mid for p in piles) > h:
                left = mid
            else:
                right = mid
        return right