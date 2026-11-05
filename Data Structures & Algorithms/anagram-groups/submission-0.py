class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for i in strs:
            print("i is", i)
            is_in = 0
            for sub in result:
                print("sub is", sub)
                if sorted(i) == sorted(sub[0]):
                    sub.append(i)
                    is_in = 1
            if is_in == 0:
                result.append([i])
            print("result is", result)
        return result
        