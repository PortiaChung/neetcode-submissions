class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        # print(nums)
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(n-2):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1]+nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            j,k = i+1,n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k-=1
                elif s < 0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return res  
                    
           

        