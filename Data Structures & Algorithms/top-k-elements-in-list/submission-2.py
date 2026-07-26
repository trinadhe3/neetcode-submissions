class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        arr = [[key,val] for key,val in freq.items()]
        arr.sort(key = lambda x : -x[1])
        for i in range(k):
            res.append(arr[i][0])
        return res