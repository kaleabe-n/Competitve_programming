class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for start,end,direction in shifts:
            if direction == 0:
                direction = -1
            prefix[start]+=direction
            if end<len(s)-1:
                prefix[end+1]-=direction
        for i in range(1,len(s)):
            prefix[i]+=prefix[i-1]
        a = ord('a')
        z = ord('z')
        ans = []
        for ind,letter in enumerate(s):
            letterOrd = ord(letter)
            letterOrd += prefix[ind]
            if letterOrd>z or letterOrd<a:
                letterOrd = (letterOrd-a)%26+a 
            ans.append(chr(letterOrd))
        return "".join(ans)
