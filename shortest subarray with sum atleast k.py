class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = []
        prefix = 0
        minLen = float('inf')
        for num in nums:
            prefix+=num
            prefixSum.append(prefix)
        prefixSum.append(0)
        monQue = deque()
        monQue.append(-1)
        for i in range(len(prefixSum)-1):
            p = prefixSum[i]
            while monQue and prefixSum[monQue[-1]]>p:
                monQue.pop()
            monQue.append(i)
            while monQue and prefixSum[monQue[-1]]-prefixSum[monQue[0]]>=k:
                minLen = min(minLen,monQue[-1]-monQue[0])
                monQue.popleft()
            
        return minLen if minLen!=float('inf') else -1
