class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(words)):
            words[i] = f(words[i])
        words.sort()
        
        ans = []
        for word in queries:
            freq = f(word)
            l = 0
            r = len(words)-1
            while l<=r:
                mid = (l+r)//2
                if freq<words[mid]:
                    r = mid-1
                else:
                    l = mid+1
            ans.append(len(words)-r-1)
        return ans
        
        
        
def f(s):
    count = [0]*26
    for letter in s:
        count[ord(letter)-ord('a')]+=1
    for i in count:
        if i > 0:
            return i
