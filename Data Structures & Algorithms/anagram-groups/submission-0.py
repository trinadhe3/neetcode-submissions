class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sstrs = [sorted(s) for s in strs]
        n = len(strs)
        check = set()
        for i in range(n):
            if i in check:continue
            else:
                curr = [strs[i]]
                check.add(i)
                for j in range(i + 1, n):
                    if sstrs[i] == sstrs[j]:
                        curr.append(strs[j])
                        check.add(j)
                res.append(curr)
        return res