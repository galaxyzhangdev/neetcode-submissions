class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        dic_sort = sorted(dic.items(), key=lambda x:x[1], reverse = True)
        print('dic is:', dic)
        print('dic_sort is:', dic_sort)
        for i in range(k):
            res.append(dic_sort[i][0])        
        return res



            