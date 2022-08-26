from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        visited = set([start])
        que = deque([start])
        while que:
            current = que.popleft()
            if arr[current] == 0:
                return True
            if arr[current]+current<len(arr) and arr[current]+current not in visited:
                visited.add(arr[current]+current)
                que.append(arr[current]+current)
            if current-arr[current]>=0 and current-arr[current] not in visited:
                visited.add(current-arr[current])
                que.append(current-arr[current])
        return False
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
