class Solution(object):
    def merge(self, intervals):
        i=0
        temp=[]
        intervals.sort()
        while i<len(intervals):
            if i!=len(intervals)-1 and intervals[i][1]>=intervals[i+1][0] :
                largest=intervals[i+1][1]
                smallest=intervals[i][0]
                if intervals[i][1]>largest:
                    largest=intervals[i][1]
                if intervals[i+1][0]<smallest:
                    smallest=intervals[i+1][0]
                temp.append(smallest)
                temp.append(largest)
                intervals.pop(i+1)
                intervals[i]=temp
                i-=1
            elif i!=0:
                temp=intervals[i]
                intervals[i]=temp
            if len(temp)==0:
                temp=intervals[i]
                intervals[i]=temp
            temp=[]
            i+=1
            
        return intervals
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
