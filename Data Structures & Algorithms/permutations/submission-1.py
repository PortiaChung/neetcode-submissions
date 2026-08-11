class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n = len(nums)
        path = [0]*n
        visited = [False]*n
        
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return
            
            for j,vis in enumerate(visited):
                if not vis:
                    path[i] = nums[j]
                    visited[j] = True
                    dfs(i+1)
                    visited[j] = False
        


        dfs(0)
        return res
        