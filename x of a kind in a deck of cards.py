class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        counts = list(counts)
        gcd = counts[0]
        for i in range(1,len(counts)):
            curr = counts[i]
            maxx = max(curr,gcd)
            minn = min(curr,gcd)
            while minn>0:
                temp = maxx
                maxx = minn
                minn = temp%minn
            gcd = maxx
            
        return gcd>1
