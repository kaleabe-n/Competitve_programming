class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        lenP = len(p)
        p = Counter(p)
        window = {}
        ans = []
        while i<len(s):
            if s[i] in window:
                window[s[i]]+=1
            else:
                window[s[i]] = 1
            if i>=lenP:
                if window[s[i-lenP]]>1:
                    window[s[i-lenP]]-=1
                else:
                    window.pop(s[i-lenP])
            if window == p:
                ans.append(i-lenP+1)
            i+=1
        return ans