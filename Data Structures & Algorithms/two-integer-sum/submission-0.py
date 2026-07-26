from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for idx,num in enumerate(nums):
            comp = target - num
            if comp in check:
                return [check[comp],idx]
            check[num] = idx
        return [-1,-1]