class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for curr in s:
            if curr.isalpha() or curr.isdigit():
                new += curr.lower()
        l,r = 0,len(new) - 1
        while l < r:
            if new[l] != new[r]:return False
            l += 1
            r -= 1
        return True