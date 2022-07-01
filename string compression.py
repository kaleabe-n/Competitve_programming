class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        ch = chars[0]
        count = 1
        while j < len(chars):
            if i == j:
                j+=1
            elif j == len(chars)-1 and chars[i] == chars[j]:
                chars.pop(j)
                count+=1
                if count>1:
                    while count>0:
                        chars.insert(j,str(count%10))
                        count = count//10
                count = 1
                j+=1
                break
            elif chars[i] == chars[j]:
                chars.pop(j)
                count+=1
            elif chars[i] != chars[j]:
                nums = 0
                if count>1:
                    while count>0:
                        chars.insert(j,str(count% 10))
                        count = count//10
                        nums+=1
                count = 1
                j+=nums
                i=j
                j+=1
        return len(chars)
    
    
