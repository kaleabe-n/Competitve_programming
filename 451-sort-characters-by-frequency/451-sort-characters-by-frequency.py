class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans=[(count[i],i) for i in count]
        ans.sort(reverse=True)
        kal=[]
        for i,j in ans:
            kal.append(j*i)
        return "".join(kal)