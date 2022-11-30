class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for item in arr:
            if item in count:
                count[item]+=1
            else:
                count[item] = 1
        return len(count.values()) == len(set(count.values()))