class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            matches = [p for p in products if p.startswith(prefix)]
            res.append(matches[:3])
        return res

