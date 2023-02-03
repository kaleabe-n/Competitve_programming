class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        down = True
        rows = [[] for _ in range(numRows)]
        row = 0
        state = True
        for letter in s:
            rows[row].append(letter)
            if state:
                if row == numRows - 1:
                    state = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    state = True
                    row += 1
                else:
                    row -= 1
        ans = ""
        for row in rows:
            ans += "".join(row)
        return ans
        