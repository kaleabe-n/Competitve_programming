class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indices =[x for x in range(len(intervals))]
        indices.sort(key=lambda x:intervals[x][0])
        ans = []
        for s,e in intervals:
            l=0
            r=len(intervals)-1
            while l<=r:
                mid = (l+r)//2
                if intervals[indices[mid]][0] >= e:
                    r=mid-1
                else:
                    l = mid+1
            if l<len(indices):
                ans.append(indices[l])
            else:
                ans.append(-1)
        return ans
        
