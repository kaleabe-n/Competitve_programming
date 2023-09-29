class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        bits = []
        for num in nums:
            currBit = []
            for _ in range(32):
                currBit.append(num&1)
                num//=2
            currBit.reverse()
            bits.append(currBit)
        for bit in bits:
            addHelper(bit,0,trie)
        maxx = 0
        for i in range(len(nums)):
            maxx = max(maxx,nums[i]^helper(0,bits[i],trie,0))
        return maxx
            
        
def helper(i,bit,trie,prevs):
    if i>=len(bit):
        return prevs
    curr = bit[i]
    prevs*=2
    if 1-curr in trie:
        return helper(i+1,bit,trie[1-curr],prevs+1-curr)
    elif curr in trie:
        return helper(i+1,bit,trie[curr],prevs+curr)
    return prevs
                             
                       
                       
def addHelper(bit,i,trie):
    if i==len(bit)-1:
        if bit[i] not in trie:
            trie[bit[i]] = {}
        return
    if bit[i] in trie:
        addHelper(bit,i+1,trie[bit[i]])
    else:
        currDict = {}
        trie[bit[i]] = currDict
        addHelper(bit,i+1,currDict)
