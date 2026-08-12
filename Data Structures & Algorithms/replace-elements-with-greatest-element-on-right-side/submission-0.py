class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]
        n = len(arr)
        lst = [-1]
        for i in range(n-2,-1,-1):
            lst.append(rightMax)
            rightMax = max(rightMax,arr[i])
        return lst[::-1]


        