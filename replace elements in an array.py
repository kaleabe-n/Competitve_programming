class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = defaultdict(bool)

        #create a dictionary that maps values to there index
        for ind in range(len(nums)):
            index[nums[ind]] = ind
        
        #iterater through the array performing the operations
        for ind,numbers in enumerate(operations):
            num1,num2 = numbers
            currInd = index[num1]
            nums[currInd] = num2
            index[num2] = currInd

        return nums
