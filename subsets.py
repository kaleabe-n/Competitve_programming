class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            temp = []
            for s in subsets:
                temp.append(s+[num])
            subsets.extend(temp)
        return subsets
