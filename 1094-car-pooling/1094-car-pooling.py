class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = 0
        for num,f,t in trips:
            maxx = max(t,maxx)
        arr = [0]*(maxx+1)
        prefix = 0
        for num,f,t in trips:
            arr[f]+=num
            if t<maxx:
                arr[t]-=num
        prefix = 0
        for i in arr:
            prefix+=i
            if prefix>capacity:
                return False
        return True
        

# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         maxLen = max([i[2] for i in trips])
#         points = [0]*(maxLen+1)
#         for i in range(len(trips)):
#             points[trips[i][1]]+=trips[i][0]
#             points[trips[i][2]]-=trips[i][0]
#         prefixSum = 0
#         for i in points:
#             prefixSum+=i
#             if prefixSum>capacity:
#                 return False
#         return True
