class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numsSet = set([str(x) for x in nums])
        reverses = set()

        for num in numsSet:
            reverse = num[::-1].lstrip("0")
            reverses.add(reverse)
            
        return len(numsSet.union(reverses))


