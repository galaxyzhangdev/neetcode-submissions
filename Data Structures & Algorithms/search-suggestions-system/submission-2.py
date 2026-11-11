class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        l, r = 0, len(products)-1
        for i, c in enumerate(searchWord):
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l+=1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r-=1
            res.append(products[l:min(l+3, r+1)])
        return res


        