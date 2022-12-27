import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        expect = {}
        for i in nums:
            if i in expect:
                if len(expect[i]) == 0:
                    heapq.heappush(expect[i+1],[1,[i]])
                else:
                    temp = heapq.heappop(expect[i])
                    temp[1].append(i)
                    temp[0]+=1
                    if (i+1) in expect:
                        heapq.heappush(expect[i+1],temp)
                    else:
                        expect[i+1] = [temp]
            else:
                if i+1 in expect:
                    heapq.heappush(expect[i+1],[1,[i]])
                else:
                    
                    expect[i+1] = [[1,[i]]]
        for i in expect:
            for j in expect[i]:
                if 0<len(j[1])<=2:
                    return False
        return True
        