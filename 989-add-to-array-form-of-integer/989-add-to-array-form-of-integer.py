class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        prev = 0
        for i in range(len(num)-1,-1,-1):
            curr = k%10+num[i]+prev
            prev = curr//10
            curr = curr%10
            ans.append(curr)
            k = k//10
        while k>0 or prev>0:
            ans.append((k%10+prev)%10)
            prev = (k%10+prev)//10
            k = k//10
        
        ans.reverse()
        return ans