class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        j = 0
        maxLen = 0
        for i in range(len(fruits)):
            if fruits[i] not in window:
                window[fruits[i]] = 1
            else:
                window[fruits[i]] += 1
            while len(window) > 2:
                if window[fruits[j]] > 1:
                    window[fruits[j]] -= 1
                else:
                    del window[fruits[j]]
                j+=1
            maxLen = max(maxLen,i-j+1)
        return maxLen
            