from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(lambda:0)
        d2 = defaultdict(lambda:0)
        for i in word1:
            d1[i]+=1
        for i in word2:
            d2[i]+=1
        k1 = list(d1.keys())
        k1.sort()
        k2 = list(d2.keys())
        k2.sort()
        v1 = list(d1.values())
        v2 = list(d2.values())
        v1.sort()
        v2.sort()
        return k1 == k2 and v1 == v2