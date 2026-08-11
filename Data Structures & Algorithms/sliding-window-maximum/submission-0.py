class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0]*(n-k+1)
        q = deque()
        left = 0
        for i,x in enumerate(nums):
            while q and x >= nums[q[-1]]:
                q.pop()
            q.append(i)

            left = i-k+1
            if left < 0:
                continue
            if q[0] < left:
                q.popleft()
            
            res[left] = nums[q[0]]
        return res

        