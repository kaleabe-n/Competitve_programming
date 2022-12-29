class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered = []
        ans = []
        for i,curr in enumerate(tasks):
            arrive,length = curr
            ordered.append([arrive,i,length])
        ordered.sort(key = lambda x:x[0])
        heap = []
        time = ordered[0][0]
        i = 0
        while i < len(ordered) or heap:
            while i < len(ordered) and ordered[i][0] <= time:
                arrive,idx,length = ordered[i]
                heapq.heappush(heap,[length,idx,arrive])
                i+=1
            if heap:
                length,index,arrive = heapq.heappop(heap)
                ans.append(index)
                time+=length
            else:
                time = ordered[i][0]
        return ans