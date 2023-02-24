class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        left = 0
        maxLen = 0
        for right,fruit in enumerate(fruits):
            if fruit in window:
                window[fruit]+=1
            else:
                window[fruit] = 1
            while len(window)>2:
                if window[fruits[left]]>1:
                    window[fruits[left]]-=1
                elif window[fruits[left]] == 1:
                    del window[fruits[left]]
                left+=1
            maxLen = max(maxLen,right-left+1)
        return maxLen


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         window = {}
#         j = 0
#         maxLen = 0
#         for i in range(len(fruits)):
#             if fruits[i] not in window:
#                 window[fruits[i]] = 1
#             else:
#                 window[fruits[i]] += 1
#             while len(window) > 2:
#                 if window[fruits[j]] > 1:
#                     window[fruits[j]] -= 1
#                 else:
#                     del window[fruits[j]]
#                 j+=1
#             maxLen = max(maxLen,i-j+1)
#         return maxLen
            
