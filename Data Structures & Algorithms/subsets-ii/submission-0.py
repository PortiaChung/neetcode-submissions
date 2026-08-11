class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        path = []

        def dfs(i):
            if i == n:
                res.append(path.copy())
                return 
            x = nums[i]
            path.append(x)
            dfs(i+1)
            path.pop()

            i+=1
            while i < n and nums[i] == x:
                i+=1
            dfs(i)
        

        dfs(0)
        return res
        