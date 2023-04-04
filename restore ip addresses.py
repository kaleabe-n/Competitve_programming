class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        helper(None,[],0,ans,s)
        return ans
        
        
def helper(num,seq,i,ans,s):
    if i>=len(s):
        if num<=255 and len(seq) == 3:
            seq = seq+[num]
            seq = [str(x) for x in seq]
            ans.append(".".join(seq))
        return
    if num == None:
        helper(int(s[0]),seq,i+1,ans,s)
    else:
        if len(seq)<=3:
            if num == 0:
                if len(seq) >= 4:
                    pass
                else:
                    helper(int(s[i]),seq+[num],i+1,ans,s)
                return
                
            if num*10+int(s[i])<=255:
                helper(num*10+int(s[i]),seq,i+1,ans,s)
            if num>=0 and num<=255 and len(seq)<3:
                helper(int(s[i]),seq+[num],i+1,ans,s)
            
        
