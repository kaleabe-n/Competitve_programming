class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxx = 1
        right = -1
        window = collections.defaultdict(int)
        while right<len(s)-1:
            right+=1
            window[s[right]]+=1
            maxx = max(maxx,window[s[right]])
            if maxx+k<(right-left+1):
                window[s[left]]-=1
                left+=1
        return right-left+1
            
            
        