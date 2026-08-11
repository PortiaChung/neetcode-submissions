class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n = len(nums)
        path = [0]*n
        on_path = [False]*n
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return 
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i+1)
                    on_path[j] = False  
        dfs(0)
        return res

        