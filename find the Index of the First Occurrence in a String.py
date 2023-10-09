class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range(len(haystack)-len(needle)+1):
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             break
        #     else:
        #         return i
        # return -1
        
        
        # if len(haystack) < len(needle):
        #     return -1
        # nHash = 0
        # for i in range(len(needle)):
        #     nHash += (ord(needle[i])+1-ord('a'))*(27**(len(needle)-i-1))
        # window = 0
        # for i in range(len(needle)):
        #     window += (ord(haystack[i])+1-ord('a'))*(27**(len(needle)-i-1))
        # if nHash == window:
        #     return 0
        # for i in range(1,len(haystack)-len(needle)+1):
        #     window -= (ord(haystack[i-1])+1-ord('a'))*(27**(len(needle)-1))
        #     window *= 27
        #     window += (ord(haystack[i+len(needle)-1])+1-ord('a'))
        #     if window == nHash:
        #         return i
        # return -1
        
        
        lsp = [0]*len(needle)
        i = 0
        j = i+1
        while j<len(needle):
            if needle[i] == needle[j]:
                lsp[j] = i+1
                i+=1
                j+=1
            else:
                if i == 0:
                    j+=1
                else:
                    i = lsp[i-1]
        i = 0
        j = 0
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lsp[j-1]
            if j == len(needle):
                return i-j
        return -1
