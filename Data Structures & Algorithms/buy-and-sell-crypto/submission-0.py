class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = float('inf')
        for pri in prices:
            minp = min(minp,pri)
            maxp = max(maxp,pri - minp)
        return maxp
