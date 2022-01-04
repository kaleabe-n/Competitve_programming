class Solution(object):
    def minSetSize(self, arr):
        arr.sort()
        freq=0
        temp=arr[0]
        frequencies=[]
        for i in range(len(arr)):
            if arr[i]==temp:
                freq+=1
            if arr[i]!=temp or i==len(arr)-1:
                temp=arr[i]
                frequencies.append(freq)
                freq=1

        i=1
        half=len(arr)/2
        frequencies.sort()
        size=0
        print(frequencies)
        while i<=len(frequencies):
            size+=frequencies[-i]
            if size>=half:
                return i
            i+=1
        """
        :type arr: List[int]
        :rtype: int
        """
        
