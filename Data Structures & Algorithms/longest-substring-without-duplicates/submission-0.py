class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        n = len(s)
        check = set()
        for r in range(n):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            res = max(res,r - l + 1)
        return res