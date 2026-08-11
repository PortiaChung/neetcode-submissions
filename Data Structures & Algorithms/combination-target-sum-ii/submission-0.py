class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        path = []

        def dfs(i,left):
            if left == 0:
                res.append(path.copy())
                return 
            if i == n or nums[i] > left:
                return 
            
            
      
           

            path.append(nums[i])
            dfs(i+1,left-nums[i])
            path.pop()

            j = i+1
            while j < n and nums[j] == nums[i]:
                j+=1
            dfs(j,left)

         

        dfs(0,target)
        return res
        