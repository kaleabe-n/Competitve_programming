class Solution(object):
    def fizzBuzz(self, n):
        answer=[]
        for i in range(1,n+1):
            st=""
            if(i%3==0):
                st+="Fizz"
                if(i%5!=0):
                    answer.append(st)
                    continue
            if(i%5==0):
                st+="Buzz"
            if(st==""):
                st+=str(i)
            answer.append(st)
        return answer
        """
        :type n: int
        :rtype: List[str]
        """
        
