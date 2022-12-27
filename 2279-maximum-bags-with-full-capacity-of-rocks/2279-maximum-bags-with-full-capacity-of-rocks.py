class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        untilFul = []
        for i in range(len(capacity)):
            untilFul.append(capacity[i]-rocks[i])
        untilFul.sort()
        i = 0
        count = 0
        while additionalRocks > 0 and i < len(capacity):
            additionalRocks -= untilFul[i]
            if additionalRocks>=0:
                count+=1
            i += 1
        return count