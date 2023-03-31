class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        added = set()
        for i in range(len(nums)):
            helper(arr,i,nums,added)
        return [x for x in arr if len(x) >= 2]
        

def helper(arr,index,nums,added):
    newArr = []
    for array in arr:
        if (array and array[-1] <= nums[index]) or not array:
            temp = array + [nums[index]]
            t = tuple(temp)
            if t not in added:
                newArr.append(temp)
                added.add(t)
    arr.extend(newArr)
