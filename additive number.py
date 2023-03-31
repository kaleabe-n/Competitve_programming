class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return helper(num,0,[],None)
        
        
def helper(num,i,seq,curr):
    if i>=len(num) and curr == None and len(seq)>2:
        return True
    elif i>=len(num):
        return False
    if curr == None:
        curr = 0    
        if num[i] == "0":
            if len(seq)>=2:
                if seq[-1]+seq[-2] == 0:
                    seq = seq+[0]
                    i+=1
                    return helper(num,i,seq,None)
                else:
                    return False
            else:
                return helper(num,i+1,seq+[0],None)
            
    if len(seq)<2:
        ans = helper(num,i+1,seq+[curr*10+int(num[i])],None)
        otAns = helper(num,i+1,seq,curr*10+int(num[i]))
        if ans or otAns:
            return True
    else:
        if seq[-1]+seq[-2] == curr*10+int(num[i]):
            return helper(num,i+1,seq+[curr*10+int(num[i])],None)
        else:
            return helper(num,i+1,seq,curr*10+int(num[i]))
    return False
    
