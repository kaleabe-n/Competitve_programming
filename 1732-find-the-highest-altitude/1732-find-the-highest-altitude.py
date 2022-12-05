class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxAlt = 0
        for i in gain:
            alt+=i
            maxAlt = max(maxAlt,alt)
        return maxAlt