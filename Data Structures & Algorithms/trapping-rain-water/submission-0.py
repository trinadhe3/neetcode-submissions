class Solution:
    def trap(self, h: List[int]) -> int:
        l,r = 1,len(h) - 2
        lh,rh = h[0],h[-1]
        water = 0
        while l <= r:
            if lh > rh:
                water += max(0,rh - h[r])
                rh = max(rh,h[r])
                r -= 1
            else:
                water += max(0,lh - h[l])
                lh = max(lh,h[l])
                l += 1
        return water
