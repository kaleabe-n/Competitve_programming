class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currChanges = {5:0,10:0}
        for bill in bills:
            if bill == 5:
                currChanges[5]+=1
            elif bill == 10:
                if currChanges[5]>0:
                    currChanges[5]-=1
                    currChanges[10]+=1
                else:
                    return False
            else:
                if currChanges[5]<=0 or (currChanges[5]<3 and currChanges[10]<=0):
                    return False
                if currChanges[10]>0:
                    currChanges[10]-=1
                    currChanges[5]-=1
                else:
                    currChanges[5]-=3
        return True
