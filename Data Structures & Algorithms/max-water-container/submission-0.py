class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr = 0
        res = 0
        n = len(heights)
        for i in range(n - 1):
            for j in range(i + 1,n):
                curr = min(heights[i],heights[j]) * (j - i)
                res = max(res,curr)
        return res