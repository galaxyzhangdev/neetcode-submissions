class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            res[tuple(tmp)].append(s)
        return list(res.values())
