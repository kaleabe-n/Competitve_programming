class Solution(object):
    def dailyTemperatures(self, temperatures):
        index = 0
        tempSta = []
        indSta = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(tempSta) == 0 or temperatures[i]<=tempSta[-1]:
                tempSta.append(temperatures[i])
                indSta.append(i)
            else:
                while True:
                    if len(tempSta)!=0:
                        if temperatures[i]>tempSta[-1]:
                            tempSta.pop()
                            tempIndex = indSta.pop()
                            ans[tempIndex] = i-tempIndex
                        else:
                            break
                    else:
                        break
                
                tempSta.append(temperatures[i])
                indSta.append(i)
        return ans
                    
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
