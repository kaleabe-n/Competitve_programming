class Solution(object):
    def carFleet(self, target, position, speed):
        carStack = []
        noOfCarFleet = 0
        posSpeed = dict(zip(position, speed))
        position.sort(reverse = True)
        for i in position:
            time = float(target-i)/posSpeed[i]
            if len(carStack) == 0 or carStack[-1]>=time:
                carStack.append(time)
            else:
                while True:
                    if  len(carStack)!=0:
                        if carStack[-1]<time:
                            carStack.pop()
                            if len(carStack)==0:
                                noOfCarFleet+=1
                        else:
                            break
                    else:
                        break
                carStack.append(time)
        if len(carStack)!=0 :
            return noOfCarFleet+1
        else:
            return noOfCarFleet
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
