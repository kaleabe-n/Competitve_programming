class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        le = len(arr)
        while le>0:
            num = arr.index(le) + 1
            if num != len(arr) and num != le:
                temp = arr[:num]
                ans.append(num)
                temp.reverse()
                arr = temp + arr[num:]
                newTemp = arr[:le]
                newTemp.reverse()
                arr = newTemp + arr[le:]
                ans.append(le)
            le-=1
        return ans
