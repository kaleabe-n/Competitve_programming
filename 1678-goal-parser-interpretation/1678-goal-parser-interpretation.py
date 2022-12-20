class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = []
        while i<len(command):
            if command[i] == "G":
                ans.append("G")
                i+=1
            elif command[i] == '(':
                if command[i+1] == "a":
                    ans.append("al")
                    i+=4
                else:
                    ans.append('o')
                    i+=2
        return "".join(ans)