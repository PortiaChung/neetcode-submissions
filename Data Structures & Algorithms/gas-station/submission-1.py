class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = 0
        res = 0
        diff = 0
        for i,(g,c) in enumerate(zip(gas,cost)):
            s += (g-c)
            if s < diff:
                diff = s 
                res = i+1
        return -1 if s < 0 else res