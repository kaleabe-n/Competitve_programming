class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}
        dictP = {}
        for letter in p:
            if letter in dictP:
                dictP[letter]+=1
            else:
                dictP[letter] = 1
        left = 0
        ans = []
        for right in range(len(s)):
            if s[right] in window:
                window[s[right]]+=1
            else:
                window[s[right]] = 1
            if right-left>=len(p)-1:
                if window == dictP:
                    ans.append(left)
                if window[s[left]]>1:
                    window[s[left]]-=1
                else:
                    del window[s[left]]
                left+=1
        return ans

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         i = 0
#         lenP = len(p)
#         p = Counter(p)
#         window = {}
#         ans = []
#         while i<len(s):
#             if s[i] in window:
#                 window[s[i]]+=1
#             else:
#                 window[s[i]] = 1
#             if i>=lenP:
#                 if window[s[i-lenP]]>1:
#                     window[s[i-lenP]]-=1
#                 else:
#                     window.pop(s[i-lenP])
#             if window == p:
#                 ans.append(i-lenP+1)
#             i+=1
#         return ans
