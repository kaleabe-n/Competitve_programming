class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        zeros = 0
        for i in range(len(num1)-1,-1,-1):
            prev = 0
            tempAns = []
            for j in range(len(num2)-1,-1,-1):
                tempAns.append(str(((int(num1[i])*int(num2[j]))+prev)%10))
                prev = (int(num1[i])*int(num2[j])+prev)//10
            if prev != 0:
                tempAns.append(str(prev))
            tempAns.reverse()
            for i in range(zeros):
                tempAns.append("0")
            zeros+=1
            tempAns = int("".join(tempAns))
            ans+=tempAns
        return str(ans)
                
                
            