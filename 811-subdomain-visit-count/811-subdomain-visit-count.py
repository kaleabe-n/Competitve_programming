class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        count = collections.defaultdict(int)
        for domain in cpdomains:
            countCurr,domain = domain.split()
            splitedDomain = domain.split(".")
            countCurr = int(countCurr)
            for i in range(len(splitedDomain)):
                temp = ".".join(splitedDomain[i:])
                count[temp]+=countCurr
        for i in count:
            ans.append(str(count[i])+ " "+ i)
        return ans
        