class Solution(object):
    def sortSentence(self, s):
        s=s.split()
        answer=""
        arr=[""]*len(s)
        for i in s:
            arr[((int(i[-1]))-1)]=i
        for i in arr:
            answer+= (i[:-1]+" ")
        return (answer.strip())

        """
        :type s: str
        :rtype: str
        """
        
