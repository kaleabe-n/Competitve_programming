class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCount = Counter(tasks)
        roundCount = 0
        
        for count in taskCount.values():
            if count % 3 == 0:
                roundCount += count /3
            elif (count - 2) % 3 == 0 and count-2 > 0:
                roundCount += (count-2)/3 + 1
            elif (count - 4) % 3 == 0 and count - 4 > 0:
                roundCount += (count-4)/3 + 2
            elif count % 2 == 0:
                roundCount += count / 2
            else:
                return -1
                
        return int(roundCount)