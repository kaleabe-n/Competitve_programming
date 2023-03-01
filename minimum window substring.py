class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = Counter(t)
        window = collections.defaultdict(int)
        leftLetters = set(t)
        left = 0
        minLen = float('inf')
        best = ""
        for right in range(len(s)):
            window[s[right]]+=1
            if window[s[right]] == tDict[s[right]]:
                leftLetters.remove(s[right])
            while len(leftLetters) == 0:
                if minLen>right-left+1:
                    minLen = right-left+1
                    best = s[left:right+1]
                window[s[left]]-=1
                if window[s[left]]<tDict[s[left]]:
                    leftLetters.add(s[left])
                left+=1
        return best
