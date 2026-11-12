class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ''
        res = []

        for c in searchWord:
            prefix = prefix + c
            matches = []
            for p in products:
                if p.startswith(prefix):
                    matches.append(p)
            res.append(matches[:3])
        return res
