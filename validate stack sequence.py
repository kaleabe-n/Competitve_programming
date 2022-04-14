class Solution(object):
    def validateStackSequences(self, pushed, popped):
        i=0
        pushCounter = 0
        popCounter = 0
        que = []
        while i<len(pushed) and pushCounter<len(pushed):
            que.append(pushed[pushCounter])
            pushCounter+=1
            if len(que)!=0:
                if popCounter>=len(popped):
                    pass
                else:
                    while popped[popCounter] == que[-1]:
                        que.pop()
                        popCounter+=1
                        if popCounter>=len(popped) or len(que)==0:
                            break
        if len(que)==0:
            return True
        else:
            return False
                
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
