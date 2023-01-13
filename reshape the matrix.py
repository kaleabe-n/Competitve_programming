class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        reshaped = []
        temp = []
        for row in mat:
            for num in row:
                if len(temp) < c:
                    temp.append(num)
                else:
                    reshaped.append(temp)
                    temp = [num]
        reshaped.append(temp)
        return reshaped
