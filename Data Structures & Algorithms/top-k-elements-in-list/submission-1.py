class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        mx = max(cnt.values())
        bucket = [[] for _ in range(mx+1)]
        for x,f in cnt.items():
            bucket[f].append(x)
        
        res = []
        for b in reversed(bucket):
            res +=b
            if len(res) == k:
                return res
        
