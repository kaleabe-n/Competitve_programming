class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indSta = []
        monSta = []
        ans = [0] *len(temperatures)
        for i in range(len(temperatures)):
            if not monSta or monSta[-1]>=temperatures[i]:
                monSta.append(temperatures[i])
                indSta.append(i)
            elif monSta[-1]<temperatures[i]:
                while monSta and monSta[-1]<temperatures[i]:
                    temp = monSta.pop()
                    ind = indSta.pop()
                    ans[ind] = i-ind
                monSta.append(temperatures[i])
                indSta.append(i)
        return ans
                    