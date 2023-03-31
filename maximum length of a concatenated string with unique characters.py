class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return helper(set(),0,0,arr)
        
def helper(prevLetters,i,length,arr):
    if i>=len(arr):
        return length
    ans1 = helper(prevLetters,i+1,length,arr)
    newSet = set(prevLetters)
    for letter in arr[i]:
        if letter in newSet:
            ans2 = 0
            break
        else:
            newSet.add(letter)
    else:
        ans2 = helper(newSet,i+1,length+len(arr[i]),arr)
    return max(ans1,ans2)
