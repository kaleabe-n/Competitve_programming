class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = self.getRow(rowIndex-1)
        ans = [1]
        for i in range(1,len(arr)):
            ans.append(arr[i-1]+arr[i])
        ans.append(1)
        return ans
