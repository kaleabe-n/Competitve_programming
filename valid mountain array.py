class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        prev = arr[0]
        increased = False
        increasing = True
        first = True
        for i in range(1,len(arr)):
            curr = arr[i]
            if curr > prev and increasing:
                prev = curr
                increased = True
            elif first and increased and prev > curr:
                first = False
                prev = curr
                increasing = False
            elif prev > curr and not increasing:
                prev = curr
            else:
                return False

        return True if not increasing else False
