class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        ans = [None]*len(people)
        for i in range(len(people)):
            count = 0
            for j in range(len(ans)):
                if people[i][1] == count and ans[j] is None:
                    ans[j] = people[i]
                    break
                if ans[j] is None or ans[j][0] == people[i][0]:
                    count+=1
        return ans