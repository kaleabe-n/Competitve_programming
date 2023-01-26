class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        firstInd = {}
        for i in range(len(s)):
            if s[i] not in firstInd:
                firstInd[s[i]] = i
        ranges = []
        for i in range(len(s)):
            if len(ranges) == 0:
               ranges.append([i,i])
            elif firstInd[s[i]]<ranges[-1][0]:
                while ranges and firstInd[s[i]]<ranges[-1][0]:
                    ranges.pop()
                if len(ranges)>0:
                    ranges[-1][1] = i
                else:
                    ranges.append([0,i])
            elif firstInd[s[i]]<=ranges[-1][1]:
                ranges[-1][1] = i
            elif firstInd[s[i]]>ranges[-1][1]:
                ranges.append([i,i])
        ans = []
        for i in ranges:
            ans.append(i[1]-i[0]+1)
        return ans
            
            
        
