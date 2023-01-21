# class Solution:
#     def pancakeSort(self, arr: List[int]) -> List[int]:
#         ans = []
#         le = len(arr)
#         while le>0:
#             num = arr.index(le) + 1
#             if num != len(arr) and num != le:
#                 temp = arr[:num]
#                 ans.append(num)
#                 temp.reverse()
#                 arr = temp + arr[num:]
#                 newTemp = arr[:le]
#                 newTemp.reverse()
#                 arr = newTemp + arr[le:]
#                 ans.append(le)
#             le-=1
#         return ans


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        length = len(arr)
        for i in range(len(arr)):
            ind = arr.index(length)
            flips.append(ind + 1)
            flips.append(length)
            left = arr[:ind+1]
            right = arr[ind+1:]
            left.reverse()
            arr = left + right
            for j in range(length//2):
                arr[j],arr[length-1-j] = arr[length-1-j],arr[j]
            length -= 1
        return flips
