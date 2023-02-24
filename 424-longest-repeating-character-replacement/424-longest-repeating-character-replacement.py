class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0]*26
        left = 0
        maxLen = 0
        for right,letter in enumerate(s):
            window[ord(letter)-ord('A')]+=1
            while (right-left+1)-max(window)>k:
                window[ord(s[left])-ord('A')]-=1
                left+=1
            maxLen = max(maxLen,right-left+1)
        return maxLen
            

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left = 0
#         maxx = 1
#         right = -1
#         window = collections.defaultdict(int)
#         while right<len(s)-1:
#             right+=1
#             window[s[right]]+=1
#             maxx = max(maxx,window[s[right]])
#             if maxx+k<(right-left+1):
#                 window[s[left]]-=1
#                 left+=1
#         return right-left+1
            
            
        
