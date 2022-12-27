class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        state = "none"
        ans = []
        temp = []
        for line in source:
            for letter in line:
                if state == "none" and letter == "/":
                    state = "changing"
                elif state == "changing" and letter == "/":
                    state = "none"
                    break
                elif state == "changing" and letter == "*":
                    state = "block"
                elif state == "changing":
                    temp.append("/")
                    temp.append(letter)
                    state = "none"
                elif state == "block" and letter == "*":
                    state = "leavblock"
                elif state == "leavblock" and letter == "/":
                    state = "none"
                elif state == "leavblock":
                    if letter != "*":
                        state = "block"
                elif state == "none":
                    temp.append(letter)
            if temp and state!="block":
                if state == "changing":
                    temp.append('/')
                    state = "none"
                if state == "leavblock":
                    state = "block"
                ans.append("".join(temp))
                temp = []
        return ans
                    
        