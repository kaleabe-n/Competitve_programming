class Solution:
    def balancedString(self, s: str) -> int:
        counts = collections.Counter(s)
        valid = len(s)//4
        invalidators = set()
        invCount = {}
        for letter in counts:
            if counts[letter]>valid:
                invalidators.add(letter)
                invCount[letter]= counts[letter]-valid
        minn = float('inf')
        l = 0
        leftLetters = set([x for x in invalidators])
        for r in range(len(s)):
            if s[r] in invalidators:
                invCount[s[r]]-=1
                if invCount[s[r]] <= 0 and s[r] in leftLetters:
                    leftLetters.remove(s[r])
            while l<len(s) and len(leftLetters) == 0:
                minn = min(minn,max(0,r-l+1))
                if s[l] in invalidators:
                    invCount[s[l]] += 1
                    if invCount[s[l]] > 0:
                        leftLetters.add(s[l])
                l+=1
        return minn
        
