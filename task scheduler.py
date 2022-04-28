class Solution(object):
    def leastInterval(self, tasks, n):
        taskCount = Counter(tasks)
        freq = sorted(taskCount.values())
        maxx = freq[-1]-1
        idles = (freq[-1]-1)*n
        noOfMax = 0
        for i in range(len(freq)-1):
            idles-= min(freq[i],maxx)
        for i in freq:
            if i == maxx+1:
                noOfMax+=1
        if idles>0:
            return idles+len(tasks)
        return len(tasks)
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
