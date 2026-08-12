class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        lst = []
        for i in range(n-1,-1,-1):
            lst.append(rightMax)
            rightMax = max(rightMax,arr[i])
        return lst[::-1]


        