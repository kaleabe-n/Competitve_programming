class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        baskets = {}
        maxLen = 0
        while j<len(fruits):
            if len(baskets) == 0:
                baskets[fruits[j]] = j
            elif len(baskets) == 1:
                baskets[fruits[j]] = j
            else:
                if fruits[j] in baskets:
                    baskets[fruits[j]] = j
                else:
                    if baskets[list(baskets.keys())[0]] > baskets[list(baskets.keys())[1]]:
                        index = baskets.pop(list(baskets.keys())[1])
                        i = index+1
                        baskets[fruits[j]] = j
                    else:
                        index = baskets.pop(list(baskets.keys())[0])
                        i = index+1
                        baskets[fruits[j]] = j
            maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen
                
