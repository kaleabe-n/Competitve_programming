class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        currTime = 0
        heap = []
        tasks = [x+[i] for i,x in enumerate(tasks)]
        tasks.sort(key = lambda x:x[0])
        i = 0
        ans = []
        while i<len(tasks) or heap:
            if heap:
                dur,ind = heapq.heappop(heap)
                ans.append(ind)
                currTime+=dur
            if not heap and i<len(tasks) and currTime<tasks[i][0]:
                currTime = tasks[i][0]
            while i<len(tasks) and tasks[i][0]<=currTime:
                heapq.heappush(heap,tasks[i][1:])
                i+=1
        return ans
            


# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         ordered = []
#         ans = []
#         for i,curr in enumerate(tasks):
#             arrive,length = curr
#             ordered.append([arrive,i,length])
#         ordered.sort(key = lambda x:x[0])
#         heap = []
#         time = ordered[0][0]
#         i = 0
#         while i < len(ordered) or heap:
#             while i < len(ordered) and ordered[i][0] <= time:
#                 arrive,idx,length = ordered[i]
#                 heapq.heappush(heap,[length,idx,arrive])
#                 i+=1
#             if heap:
#                 length,index,arrive = heapq.heappop(heap)
#                 ans.append(index)
#                 time+=length
#             else:
#                 time = ordered[i][0]
#         return ans
