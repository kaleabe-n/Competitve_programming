class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot = 0
        equalToPivot = 0
        greaterThanPivot = 0

        #count the number less than equal to and greater than pivot
        for num in nums:
            if num < pivot:
                lessThanPivot += 1
            elif num == pivot:
                equalToPivot += 1
            else:
                greaterThanPivot += 1
        lp = 0
        ep = lessThanPivot
        gp = lessThanPivot + equalToPivot
        numsRearenged = [None] * len(nums)

        #insert the numbers in there place
        for num in nums:
            if num < pivot:
                numsRearenged[lp] = num
                lp += 1
            elif num == pivot:
                numsRearenged[ep] = num
                ep += 1
            else:
                numsRearenged[gp] = num
                gp +=1

        return numsRearenged
