class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        check = set()
        res = []
        n = len(nums)
        for i in range(n - 2):
            l , r = i + 1,n - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0 and (nums[i],nums[l],nums[r]) not in check:
                    res.append([nums[i],nums[l],nums[r]])
                    check.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif curr > 0:
                    r -= 1
                else :
                    l += 1
        return res
