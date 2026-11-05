class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            print("i is:", i)
            j = 0
            prod = 1
            print("before j is:", j)
            while j < len(nums):
                if j == i: 
                    j += 1
                else:
                    print("j is:", j)
                    print("nums[j] is:", nums[j])
                    print("before prod is", prod)
                    prod = prod * nums[j]
                    print("prod is:", prod) 
                    j += 1
            res.append(prod)
        return res
        