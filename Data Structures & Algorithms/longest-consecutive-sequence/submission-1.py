class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        check = set(nums)
        res = 0
        for num in check:
            if num - 1 not in check:
                curr = num
                while curr + 1 in check:
                    curr += 1
                res = max(res,curr - num + 1)
        return res