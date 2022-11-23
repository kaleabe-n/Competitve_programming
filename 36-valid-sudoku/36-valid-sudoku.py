class Solution(object):
    def isValidSudoku(self, board):
        nums = {}
        for rowNum,row in enumerate(board):
            for colNum,item in enumerate(row):
                if item in nums:
                    if item!="." and(rowNum in nums[item]['row'] or colNum in nums[item]["col"]):
                        return False
                    nums[item]['row'].append(rowNum)
                    nums[item]['col'].append(colNum)
                    if item!="." and rowNum//3*3+colNum//3 in nums[item]['sub']:
                        return False
                    nums[item]['sub'].append(rowNum//3*3+colNum//3)
                else:
                    nums[item] = {'row':[rowNum],'col':[colNum],'sub':[rowNum//3*3+colNum//3]}
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        