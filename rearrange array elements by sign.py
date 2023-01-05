class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        orderedList = []
        leftPositive = -1
        leftNegative = -1
        #add the left most negative and positive values to a list in there respective order 
        while len(orderedList) < len(nums):
            
            #find left most positive number
            while leftPositive < 0 or (leftPositive < len(nums) and nums[leftPositive] < 0):
                leftPositive += 1

            #find left most negative number
            while leftNegative < 0 or (leftNegative <len(nums) and nums[leftNegative] > 0):
                leftNegative += 1

            #add leftmost positive number
            if len(orderedList) % 2 == 0:
                orderedList.append(nums[leftPositive])
                leftPositive += 1

            #add left most positive number
            else:
                orderedList.append(nums[leftNegative])
                leftNegative += 1
        
        return orderedList
