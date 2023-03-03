class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n==1:
                return ["0"]
            else:
                temp = helper(n-1)
                temp2 = []
                for i in temp:
                    if i=="0":
                        temp2.append("1")
                    else:
                        temp2.append("0")
                temp2.reverse()
                temp.append("1")
                temp.extend(temp2)
                return temp 
            
        ans = helper(n)
        return ans[k-1]
