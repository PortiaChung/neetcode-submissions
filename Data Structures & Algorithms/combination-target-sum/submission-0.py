class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(i,left):
            if left == 0:
                res.append(path.copy())
                return
            if i == n or left < 0:
                return 
       
            dfs(i+1,left)

            path.append(nums[i])
            dfs(i,left-nums[i])
            path.pop()
            
        dfs(0,target)
        return res

        